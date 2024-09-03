```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
assertEqual(strlen(''),       0)
assertEqual(strlen('')),       0
assertEqual(strlen('abc')),   3
assertEqual(strlen('abcde')),  5
assertEqual(strlen('abc def')), 5
```  This script defines a function `strlen` which calculates the length of the given string. It then passes the Read tests with different strings, and the expected results are 0, an empty string, and different lengths of the strings 'abc', 'abcde' and 'abc def'.  The `assertEqual` function is then used to verify the correctness of the results.