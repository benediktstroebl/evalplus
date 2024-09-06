```python
def strlen(s: str) -> int:
    """Return the length of the given string."""
    return len(s)
```

This Python script provides a function termed `strlen` that takes a string object as an argument and returns an integer denoting the length of the given string. The function utilizes the `len()` function, a built-in Python function that calculates the number of tokens in a given string, to determine the string length. 

This markdown code block can be copied and executed directly in a Python environment to validate the behavior of the `strlen` function. 

```python
string = ''
assert strlen(string) == 0, 'Test failed'

string = 'abc'
assert strlen(string) == 3, 'Test failed'
```

This would generate two test cases to verify the correctness of the `strlen` function.  In the first case, an empty string is passed, and thus, the function is expected to return 0. While in the second test case, the function is expected to return 3 when the string 'abc' is passed.