```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```

The function leverages the intersection of sets to identify common characters between two strings, s0 and s1. To handle cases with varying lengths gracefully, we calculate the similarity score as the ratio of the number of common characters to the minimum length of the two strings, filtered by a threshold of 0.6. This ensures that at least 60% of the characters in one string match the characters in the other string, considering all possible permutations.