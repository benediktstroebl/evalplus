```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a new string where all alphabetic characters have been flipped between lowercase and uppercase. The `join` function is utilized to amalgamate the altered characters back into a single string.

To verify the functionality, you can test it with the provided example string "Hello" to get the desired output "hELLO".