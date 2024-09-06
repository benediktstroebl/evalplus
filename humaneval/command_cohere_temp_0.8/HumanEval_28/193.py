```python
# Retrieve the requested script
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result = ''
    for string in strings:
        result += string
    return result
```
The `concatenate` function takes a list of strings (`List[str]`) as input and returns a single string that concatenates all the inputs together. It achieves this by using a for loop to iterate over each string in the input list and appending each string to a result string. The loop starts with an empty result string, ensuring that the initial value is correct for handling an empty input list. For an empty input list, the function returns an empty string, matching the specified behavior. Lastly, the function is fully self-contained within the defined main block, making sure that it can be run as a standalone script to test or use in the future.