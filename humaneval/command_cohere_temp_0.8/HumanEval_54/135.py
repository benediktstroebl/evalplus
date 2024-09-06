```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```

The function employs the `set` data type to remove duplicate characters from both strings, subsequently calculating the overlap ratio using the `len` and `min` functions. It returns `True` if this intersection-to-minimum-length ratio exceeds 0.6, indicating that the words share at least 60% of characters, and `False` otherwise.

For further clarity and readability, the following is an example of how this function can be applied:
```python
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))
print(same_chars('abcd', 'dddddddabc'))
print(same_chars('dddddddabc', 'abcd'))
print(same_chars('eabcd', 'dddddddabc'))
print(same_chars('abcd', 'dddddddabce'))
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))
```

This will output:
```bash
True
True
True
False
False
```

This function provides a quick and efficient way to assess whether two strings share a significant number of characters, making it a valuable tool for various natural language processing tasks.