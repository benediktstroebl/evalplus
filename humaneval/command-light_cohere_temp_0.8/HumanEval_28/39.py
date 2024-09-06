Here's a self-contained Python function that solves the problem of joining a list of strings into a single markdown code block:
```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    >>> strings = ['##', '\n', 'hello']
    >>> concatenate(strings)
    '##hello\n'
    """

    # Use str.format to add new line feed
   
    result = ''.join(format(str(s) for s in strings))
    return result
```

This function takes a list of strings as an input and uses the join() function with the `str.format` function to ensure proper line breaks. The `result` variable stores the string with all the elements of the input list concatenated.