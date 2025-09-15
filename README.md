# Constitutional Similarity Analysis

In light of recent political unrest in Nepal—and some discussions about its flaws— I grew curious: **which other constitutions in the world are most similar to Nepal’s, and do they face similar political challenges?**

This Saturday, after a quiet afternoon cup of tea, I decided to explore.

## Data Collection

I discovered a website hosting **204 of the most recent constitutions worldwide**. Downloading them one by one? Not happening.  
So, I automated the process using:

- **Selenium**
- **webdriver_manager**
- **BeautifulSoup**

This gave me a complete dataset of constitutions in PDF form.

## Methodology

Steps:
1. **Chunking**: Split each constitution into overlapping chunks (~200 words each) to preserve context.  
2. **Embedding**: Used **sentence-transformer models** (`all-MiniLM-L6-v2`, `all-mpnet-base-v2`) to embed chunks.  
   - Directly embedding a full constitution = too long, too noisy.  
   - Chunking ensures semantic similarity works better.  
3. **Aggregation**: Took the **mean of all chunk embeddings** to represent an entire constitution.  
4. **Similarity Search**: Ran **cosine similarity (top-k nearest neighbor)** across constitutions.
 

## Reflections

I’m a systems guy, and usually skeptical about Language Models **(and honestly don't know much about them)**. So, my methodology is just a proof of concept.
For someone interested in - **Politics**, **Constitutional law**, **and AI applied to social science** I believe this is a fun project to explore further. 

---
