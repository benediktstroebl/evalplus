```python
def concatenate(strings: List[str]) -> str:
    """ Concatenenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenated string
    """
    return "".join(strings)

def test_concatenate():
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The code defines a function **`concatenate`** that takes a list of strings as an argument and returns the concatenated result as a single string. 

This function uses the list comprehension to iterate through the input strings and concatenate them with a space character (' ').  The test function **`test_concatenate`** checks the correctness of the **`concatenate`** function by passing various test cases and asserting the expected output.   The expected results are the same as the function definition.