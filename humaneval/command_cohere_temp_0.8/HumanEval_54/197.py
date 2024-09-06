```python
def same_chars(s0, s1):
    return sorted(s0) == sorted(s1)
```

The `same_chars` function uses sorting to ensure that characters in two strings are compared in the same order. This approach allows quick detection of equality regardless of the string's actual layout in memory.