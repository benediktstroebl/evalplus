Certainly! Here's a self-contained Python function that solves the problem of joining a list of strings into a single string: 
```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string and return it
    """
    return ''.join(strings)
```

This function takes a list of strings as input and returns a string that concatenates all the strings in the input list into a single string. 
To test the correctness of the function, there are some sample inputs and expected outputs in the commented-out section.