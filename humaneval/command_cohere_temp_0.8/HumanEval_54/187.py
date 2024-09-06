```python
def same_chars(s0, s1):
    return sorted(s0) == sorted(s1)
```

The above `same_chars` function works by sorting all characters in both words using the `sorted()` function, which ensures that characters appear in the same order in both strings. Then, it compares the sorted versions of both words to determine if they are the same, ultimately determining whether the two words have the same characters.