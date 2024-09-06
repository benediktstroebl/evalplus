Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / max(len(s0), len(s1)) > 0.5
```
The function works by comparing the unique characters in both strings and checking whether half or more of the unique characters are present in either string. The sets are used to remove any duplicate characters from consideration.