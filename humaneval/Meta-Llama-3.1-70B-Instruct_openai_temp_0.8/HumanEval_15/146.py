```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

In this script, we define the `string_sequence` function as specified. The `join` method is used to concatenate the numbers in the range from 0 to `n` (inclusive) into a single string, with spaces in between each number.

The `doctest` module is used to test the function with the provided test cases. The `testmod` function runs all the doctests in the current module. If the tests pass, it does not produce any output. If the tests fail, it reports the failure.