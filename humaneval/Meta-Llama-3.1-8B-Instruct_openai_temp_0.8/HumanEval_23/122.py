Here is a self-contained Python script that meets your requirements:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    # Use Python's built-in len function to get the length of the string
    return len(string)

# Test the function with doctest
import doctest

doctest.testmod()
```
Let me explain what's going on in this script:

* The `strlen` function is defined as before, but it simply uses the built-in `len` function to get the length of the string.
* The `doctest` module is used to automatically run the doctest-style comments at the top of the function. The `testmod()` function is called at the end to run the tests.

When you run this script, it should print nothing to the console, indicating that the tests passed. If you change the `strlen` function to return an incorrect value, you should see an error message when you run the script.