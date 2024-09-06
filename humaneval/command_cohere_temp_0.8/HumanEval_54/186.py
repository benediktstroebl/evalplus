```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```

The problem is to check whether two strings have approximately the same characters. To solve it, we compare the sets of characters in both strings and then calculate the fraction of common characters. Finally, we check if this fraction is greater than 0.6, which implies that at least 60% of the characters are the same.