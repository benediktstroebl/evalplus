Here's a Python script with a self-contained function that solves the problem:
```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```
This function employs the sets intersection operation to detect shared characters between the two strings. Subsequently, it calculates the fraction of common characters divided by the minimum of the lengths of both strings. If this fraction exceeds 0.6, the function returns True, indicating that the two words share a substantial proportion of characters and are potentially rearrangements of each other. Otherwise, it returns False, suggesting distinct character sets. 
The expected behavior for the provided test cases is:
```
True
True
True
False
False
False
```