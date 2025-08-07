# Email Domain Extractor

This is a simple Python project that extracts email domains from a list of email addresses using regular expressions.

## 📌 What it does
Given a list of email addresses, it extracts and prints just the domain part (e.g., `gmail.com`, `yahoo.com`, etc.).

## 🔧 How it works
The script uses `re.findall()` to extract the domain from each email using the following pattern:
```python
@([\w\.]+)
