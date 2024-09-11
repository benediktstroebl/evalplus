```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)
```

You can run this script in your Python environment and test the `strlen` function with different inputs to see how it works. 

However, please note that Python already has a built-in `len` function to get the length of strings, lists, and other iterables, so this custom function might be unnecessary unless you have specific requirements or constraints that necessitate creating your own. 

Here's how you might test this function in your Python script:
```python
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```

This will print the length of the strings `""` and `"abc"`, verifying that the `strlen` function is working as expected.