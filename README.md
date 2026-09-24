# AI Recommendation Logic — Project 3

Internship project for **DecodeLabs** (Industrial Training Kit, Batch 2026).

## Overview

A content-based recommendation engine built in Python — the "Tech Stack Recommender." Instead of fixed rules (Project 1) or predicting a category from labeled data (Project 2), this project matches a user's input against a set of items using similarity logic, the same core idea behind real-world recommendation engines like Netflix or Amazon.

Given a user's skills, the script recommends the job roles that best match those skills.

## How It Works

1. **Dataset** — a small set of job roles, each described by a list of associated skills (standing in for a `raw_skills.csv` dataset).
2. **Vectorization** — skills and roles are converted into numeric vectors using `TfidfVectorizer`, which gives more weight to specific/rare skills and less weight to common ones.
3. **User input** — the user enters 3 skills.
4. **Cosine similarity** — measures how closely the user's skill vector aligns with each role's vector, regardless of the size of either list.
5. **Ranking** — scores are sorted, and the Top 3 matching roles are returned with a percentage match.

## How to Run

```bash
python Project-03.py
```

You'll be prompted to enter 3 skills one at a time.

## Example

```
Enter skill 1: Python
Enter skill 2: Cloud Computing
Enter skill 3: Automation

Top 3 Recommended Career Paths:
Cloud Architect - 51.71% match
System Administrator - 18.4% match
Data Scientist - 15.22% match
```

## Tech Used

- Python 3
- scikit-learn (TfidfVectorizer, cosine_similarity)

## Author

Part of the DecodeLabs AI Engineering Internship — Batch 2026.
