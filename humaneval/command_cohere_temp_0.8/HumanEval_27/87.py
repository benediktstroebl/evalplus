```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that takes a string as an input and returns a string with flipped case, where all lowercase characters are flipped to uppercase and all uppercase characters are flipped to lowercase. This is achieved through a generator expression that processes each character in the input string. The `swapcase()` method is used for characters that are alphabetic, while non-alphabetic characters like punctuation marks or spaces are left unchanged. 

To test this script, you can call the `flip_case` function with different input strings and compare the output with the desired results. 

Let me know if you'd like to discuss further or have any other questions!