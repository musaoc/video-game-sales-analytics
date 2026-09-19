# Video Game Sales Analytics — 40 Years of Gaming Industry Data

A comprehensive video game industry analytics project examining sales of over 16,500 titles across four decades, highlighting platform dominance, genre shifts, and regional consumer behavior.

[![Kaggle Notebook](https://img.shields.io/badge/Kaggle-Notebook-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/code/lazer999/video-game-sales-analysis-for-gamers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Field](https://img.shields.io/badge/Field-Exploratory%20Data%20Analysis%20/%20Interactive%20Visualization-brightgreen)](#)

---

## Table of Contents
- [Project Overview](#project-overview)
- [Key Highlights & Results](#key-highlights--results)
- [System Architecture & Workflow](#system-architecture--workflow)
- [Repository Structure](#repository-structure)
- [Quickstart & Reproduction](#quickstart--reproduction)
- [Dataset Details](#dataset-details)
- [Author & Acknowledgments](#author--acknowledgments)

---

## Project Overview

This repository provides the complete, production-structured implementation of the **[Video Game Sales Analytics — 40 Years of Gaming Industry Data](https://www.kaggle.com/code/lazer999/video-game-sales-analysis-for-gamers)** project originally published on Kaggle. 

The primary focus of this work is translating complex data into actionable machine learning solutions using disciplined data engineering, rigorous validation strategies, and clean, leak-free preprocessing pipelines.

---

## Key Highlights & Results

- Comprehensive study of 16,500+ commercial titles spanning 1980 through 2020.
- Cross-generation platform comparisons (Nintendo, PlayStation, Xbox, Atari, PC).
- Regional sales dissection contrasting North American, European, Japanese, and Global preferences.
- Interactive Plotly charts and Seaborn distributions detailing top publishers and blockbuster titles.

---

## System Architecture & Workflow

The pipeline follows a structured, modular execution path:

```mermaid
flowchart LR
    A[16,500+ Commercial Game Records] --> B[Data Wrangling & Categorization]
    B --> C[Platform Wars: PlayStation vs Nintendo vs Xbox]
    B --> D[Regional Market Shifts: NA vs EU vs JP]
    B --> E[Genre Dominance Across Decades]
    C --> F[Strategic Industry Intelligence]
    D --> F
    E --> F
```

---

## Repository Structure

```plaintext
video-game-sales-analytics/
├── notebooks/
│   └── video-game-sales-analytics.ipynb      # Original Jupyter notebook with full exploratory visuals
├── src/
│   └── main.py                # Modular, executable Python pipeline
├── .gitignore                 # Standard Python/Jupyter ignores
├── LICENSE                    # MIT License
├── README.md                  # Human-friendly documentation
└── requirements.txt           # Verified Python dependencies
```

---

## Quickstart & Reproduction

### 1. Clone the Repository
```bash
git clone https://github.com/musaoc/video-game-sales-analytics.git
cd video-game-sales-analytics
```

### 2. Set Up a Virtual Environment
```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Pipeline
You can run the end-to-end script directly:
```bash
python src/main.py
```

Or open and run the interactive notebook:
```bash
jupyter lab notebooks/video-game-sales-analytics.ipynb
```

---

## Dataset Details

- **Dataset / Competition**: [Video Game Sales (vgchartz)](https://www.kaggle.com/datasets/gregorut/videogamesales)
- **Origin Platform**: Kaggle
- For automated dataset downloading via Kaggle CLI:
  ```bash
  kaggle datasets download -d gregorut/videogamesales
  ```

---

## Author & Acknowledgments

- **Author**: **Muhammad Musa Khan** (Kaggle Master)
- **Kaggle Profile**: [@lazer999](https://www.kaggle.com/lazer999)
- **GitHub**: [@musaoc](https://github.com/musaoc)
- **Original Kaggle Solution**: [Video Game Sales Analytics — 40 Years of Gaming Industry Data](https://www.kaggle.com/code/lazer999/video-game-sales-analysis-for-gamers)

If you found this project helpful or insightful, please consider starring the repository ⭐!
