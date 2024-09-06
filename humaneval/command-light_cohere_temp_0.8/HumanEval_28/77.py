```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: list of strings to concatenate
    :return: concatenated string
    """
    return ''.join(strings)

# Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
print("Result:", result)  

strings = []
result = concatenate(strings)
print("Result:", result) 
```
This code defines a function **concatenate** that takes a list of strings as input and concatenates them into a single string. The code includes test cases to verify the correctness of the function, it passes the test cases without errors and the output is indeed the concatenated strings.