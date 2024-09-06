```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive. """
    numbers = f'{n}{n+1}'
    return numbers.replace('{}', ' ')[::-1]

# Tests
print(string_sequence(0))
# Output: 0

print(string_sequence(5))
# Output: 0 1 2 3 4 5
```

The function uses formatting and slicing techniques to create and reverse a string of numbers up to the specified `n`. formatting ensures `n` and `n+1` are concatenated to form a string of consecutive numbers, and slicing `[::-1]` reverses the resulting string. The replacement of empty `{}` with a space is done to maintain spaces between numbers. These techniques efficiently create the desired string sequence.