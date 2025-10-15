import pandas as pd
from jira import JIRA
from datetime import datetime

JIRA_URL = "https://your-instance.atlassian.net"
JIRA_USER = "you@example.com"
JIRA_TOKEN = "your_token"

jira = JIRA(server=JIRA_URL, basic_auth=(JIRA_USER, JIRA_TOKEN))
issues = jira.search_issues("project=XYZ", maxResults=1000, expand='changelog')

data = []
for issue in issues:
    stages = {}
    analysis_start, dev_start, code_review_start, testing_start = None, None, None, None

    for history in issue.changelog.histories:
        for item in history.items:
            # Detect status changes and stage entry dates (pseudo-code)
            if item.field == "status":
                if item.toString == "In Analysis":
                    analysis_start = history.created
                if item.toString == "In Development":
                    dev_start = history.created
                if item.toString == "Code Review":
                    code_review_start = history.created
                if item.toString == "Testing":
                    testing_start = history.created

    # Calculations (example: simple intervals if dates present)
    durations = {}
    if analysis_start and dev_start:
        durations["analysis_days"] = (pd.to_datetime(
            dev_start) - pd.to_datetime(analysis_start)).days
    if dev_start and code_review_start:
        durations["dev_days"] = (pd.to_datetime(
            code_review_start) - pd.to_datetime(dev_start)).days
    # etc. for each stage...

    # Record all useful fields
    row = {
        "key": issue.key,
        "summary": issue.fields.summary,
        "assignee": getattr(issue.fields.assignee, 'displayName', None),
        "status": issue.fields.status.name,
        "analysis_days": durations.get("analysis_days"),
        "dev_days": durations.get("dev_days"),
        # ... continue fields
    }
    data.append(row)

df = pd.DataFrame(data)
df.to_excel("output/jira_export.xlsx", index=False)
df.to_csv("output/jira_export.csv", index=False)

print("Export complete!")
