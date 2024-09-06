```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that takes a string as an argument and flips the case of alphabetic characters only, retaining all non-alphabetic characters in their original case. 

To use this function, simply call it with a string as an argument, and it will return the string with flipped case for alphabetic characters. 

For example, running the function with the input `'Hello There, World!'` would yield the output `'hELLO There, wORLD!'`. 

This is demonstrated in the provided example test case. 

Feel free to experiment with different inputs and examine the results to understand how the function adapts to different scenarios.