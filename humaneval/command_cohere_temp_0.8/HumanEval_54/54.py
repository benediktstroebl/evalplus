Here's a Python script with a self-contained function that solves the problem:
```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```
The function `same_chars()` takes two strings as input and returns a boolean indicating whether the strings have roughly the same characters distributed throughout them. It does this by checking whether the intersection of characters in both strings contains at least 60% of the minimum length of either string.