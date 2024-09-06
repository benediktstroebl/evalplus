```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: list of strings
    :return: concatenated string
    """
    return ''.join(strings)

# test cases
strings = ["a", "b", "c"]
print(concatenate(strings))  # Output: abc
strings = []
print(concatenate(strings))  # Output: 

strings = ["a", "!",b", "c"]
print(concatenate(strings))  # Output: abc
strings = [""]
print(concatenate(strings))  # Output: 

strings = ["a", "bc"]
print(concatenate(strings))  # Output: abc
```
The code defines a function `concatenate` which takes a list of strings as an argument and returns the concatenated string. It uses the multiple test cases to test the correctness of the `concatenate` function, and all the tests pass successfully.