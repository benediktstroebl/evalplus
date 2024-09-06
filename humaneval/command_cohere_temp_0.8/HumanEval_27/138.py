```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a string with flipped case, ensuring that non-alphabetic characters remain unchanged. The `join` method is used to concatenate the modified characters back together into a single string.

To execute this code and test the function, save it to a `.py` file (e.g., `flip_case.py`) and run it using a Python interpreter. You can also import the function into another Python script to utilize its functionality. 

**Note:** This solution is concise and effective for general strings. However, considering edge cases and handling punctuation separately may be advisable depending on your specific use case.