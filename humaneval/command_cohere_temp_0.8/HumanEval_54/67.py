Here's a Python script with a self-contained function that solves the problem:
```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```
This function employs the sets intersection operation to detect shared characters between the two strings. Subsequently, it calculates the fraction of common characters and compares it to 0.6, representing an arbitrary threshold for evaluating whether the two strings share a substantial majority of characters.