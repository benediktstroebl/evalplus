```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.
    """
    return len(string)
```

This Python script provides a function (`strlen`) that takes a string as input and returns the length of that string. The function leverages the `len()` function, which is a built-in Python function that returns the number of items in a container, to calculate the length of the input string. 

If no argument is provided, this function will return the length of the string 'None'. 

This approach aligns with the problem statement's requirement and maintains code simplicity since it uses a built-in function rather than rewriting the length determination logic. 

To validate the correctness of this function, ensure that your tests cover both empty and non-empty strings since they have distinct behavior at the edge. Additionally, consider testing strings of varying lengths to ensure the function behaves as expected for different cases.