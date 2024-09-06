```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that takes a string as an input and returns a string with flipped case, ensuring that non-alphabetic characters remain unchanged. This is achieved by using a list comprehension that iterates through each character in the input string. For alphabetic characters, `swapcase()` is used to exchange uppercase with lowercase and vice versa. Meanwhile, non-alphabetic characters like digits or special symbols are preserved in their original form. The final output is a string with flipped case for alphabetic characters and unchanged characters for non-alphabetic characters. 

Here is an example usage of this function:
```python
input_string = "Hello, World!"
result = flip_case(input_string)
print(result)  # Output: "hELLO, wORLD!"
``` 

This will produce the expected result of flipping the case of the alphabetic characters in the input string while keeping non-alphabetic characters unchanged.