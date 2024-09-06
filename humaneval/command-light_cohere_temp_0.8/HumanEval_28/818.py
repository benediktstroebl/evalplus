```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Returns: concatenated string
    """
    return ''.join(strings)

# Test the function with different inputs
strings = ["a", "b", "c"]
assertEqual(concatenate(strings), "abc")
strings = [""]
strings += ["a", "bc"]
assertEqual(concatenate(strings), "abc")
strings = ["a", "bc", "d"]
assertEqual(concatenate(strings), "abcd")
```
The function concatenate in this code takes a list of strings as input and concatenates them into a single string. The returned string is then joined using the join() method. The test cases ensure that the function is working correctly with different inputs.