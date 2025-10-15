# Jira Agile Analytics Exporter

## Overview
A Python tool to extract Jira issue data, automatically calculate Agile delivery metrics (cycle time, lead time, velocity, DORA, investment tracking), and export analytics-ready datasets (Excel/CSV) for reporting in Power BI, Tableau, Looker, Google Sheets, etc.

## Features
- Extracts Jira workflow transitions ("In Development", "Code Review", "Testing", etc.) and computes duration for each stage.
- Auto-generates columns for flow status, stage start/end dates, cycle time, lead time, sprint velocity.
- Optionally integrates Google Gemini (or similar LLM) to classify or auto-tag issues, automate PMO admin, and enhance dataset.
- Produces a full Excel/CSV export, ready for visualization.
- Supports DORA metrics: lead time, mean time to recover, deployment frequency, change failure rate.
- Tracks investment allocation by label/epic, backlog movements, sprint completion, team throughput.

## Quick Start
1. `pip install -r requirements.txt`
2. Update `config.yaml` with Jira domain, token, field mappings.
3. Run:
