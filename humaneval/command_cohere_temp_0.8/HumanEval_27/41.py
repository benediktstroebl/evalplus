```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that takes a string as an input and returns a string with flipped cases for alphabetical characters. The `swapcase` function is utilized to invert the case of alphabetic characters, while non-alphabetic characters like punctuation marks or digits are left unchanged.

Here is an example usage of the function:
```python
print(flip_case("Hello, World!"))  # Outputs: "hELLO, wORLD!"
```

This will swap the cases of the alphabetic characters 'H', 'e', 'L', 'l', 'o', ',', and 'W', while leaving non-alphabetic characters unchanged, thus resulting in the output "hELLO, wORLD!" 

The code efficiently executes the task of flipping character cases while maintaining consistency for alpha and non-alpha characters.