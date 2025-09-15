# Constitutional Similarity Analysis

In light of recent political unrest in Nepal—and the growing debate about whether its constitution might be partly responsible—I grew curious: **which other constitutions in the world are most similar to Nepal’s, and do they face similar political challenges?**

This Saturday, after a quiet afternoon cup of tea, I decided to explore.

## Data Collection

I discovered a website hosting **204 of the most recent constitutions worldwide**. Downloading them one by one? Not happening.  
So, I automated the process using:

- **Selenium**
- **webdriver_manager**
- **BeautifulSoup**

This gave me a complete dataset of constitutions in PDF/text form.

## Methodology

Reading hundreds of pages manually was out of the question. Instead, I turned to **text processing and embeddings**.

Steps:
1. **Chunking**: Split each constitution into overlapping chunks (~1000 words each) to preserve context.  
2. **Embedding**: Used **sentence-transformer models** (`all-MiniLM-L6-v2`, `all-mpnet-base-v2`) to embed chunks.  
   - Directly embedding a full constitution = too long, too noisy.  
   - Chunking ensures semantic similarity works better.  
3. **Aggregation**: Took the **mean of all chunk embeddings** to represent an entire constitution.  
4. **Similarity Search**: Ran **cosine similarity (top-k nearest neighbor)** across constitutions.

## Findings

The results were fascinating:  
- Some constitutions show **surprising structural and linguistic similarities** to Nepal’s.  
- These overlaps could help explain shared political challenges or patterns of instability.  

## Reflections

I’m a computer systems researcher, and usually skeptical about the hype around LLMs.  
But in this case—even if sentence transformers are just “glorified autocomplete”—they uncovered insights I would never have spotted manually.  

## Why This Matters

For anyone interested in:
- **Politics**
- **Constitutional law**
- **AI applied to social science**

…this project is a fun and eye-opening exploration.

---
