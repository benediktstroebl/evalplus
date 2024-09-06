```python
def same_chars(s0, s1):
    return sorted(s0) == sorted(s1)
```

The above `same_chars` function employs the `sorted` function to sort the characters in two strings and then compare them. This approach enables a quick comparison of the characters irrespective of the string's original order. The solution is concise and effective in determining if two strings share the same characters.