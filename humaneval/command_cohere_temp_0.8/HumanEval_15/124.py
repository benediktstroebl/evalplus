```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This code snippet includes the function `string_sequence` as described in the prompt and provides tests as examples of function usage. 

Do these results match your expected output? Is there anything else I can help you with? I can also explain some of the underlying concepts if needed.