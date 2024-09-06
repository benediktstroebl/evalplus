Here's a Python script with a self-contained function that solves the problem:
```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```
This function employs the set membership test to identify common characters in two strings and then calculates the fraction of common characters, normalized by the minimum length of the two strings. The result is considered a match if this fraction exceeds 0.6, indicating that the strings share a sufficient proportion of characters.