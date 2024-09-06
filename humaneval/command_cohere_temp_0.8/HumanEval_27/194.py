```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() if char.isalpha() else char for char in string)
```

This script provides a function that takes a string as input and returns a new string where all lowercase characters are flipped to uppercase and all uppercase characters are flipped to lowercase. This function achieves this by using a list comprehension that checks if each character is alphabetic using the `isalpha()` string method, and then uses the `swapcase()` method to flip the case if the character is alphabetic. For non-alphabetic characters, the character remains unchanged in the final string. 

The above solution is efficient and correctly flips the case for all characters while keeping non-alphabetic characters unaffected.