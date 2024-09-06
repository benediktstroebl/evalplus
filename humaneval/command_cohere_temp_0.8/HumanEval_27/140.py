```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as input and returns a string where the case of letters has been flipped, while leaving non-alphabetic characters unchanged. The `join` method is utilized to concatenate the string parts into a single string, with each character possibly undergoing a case flip or remaining as it is.

To test this function, you can create a string input and pass it to the function. The function will return the flipped string. You can verify the results by checking if the characters have been correctly flipped. For instance, with the input `Hello Cohere!`, the expected result would be `hELLO COHERE!`.