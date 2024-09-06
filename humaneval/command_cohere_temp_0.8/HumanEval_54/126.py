```python
def same_chars(s0, s1):
    return sorted(s0) == sorted(s1)
```

The idea is to sort the characters in the strings and then compare them. If the characters are the same, then the two strings have the same composition.