```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```

The function employs set theory and the proportion of common characters to determine whether two strings have a similar character distribution, considering upper, lower, and digit cases. It's clarified through tests that tackle various scenarios of matching and differing characters, delivering a robust and adaptable solution.