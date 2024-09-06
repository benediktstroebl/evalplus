```python
def same_chars(s0, s1):
    return sorted(s0) == sorted(s1)
```

The function `same_chars` works by sorting all characters from both strings and comparing if they are the same. In effect, it checks if the characters in both strings are the same, regardless of their placement. This solution is concise and straightforward, making it optimal for this specific problem.