```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() if char.isalpha() else char for char in string)
```

This script provides a function that accepts a string as an argument and returns a new string where each lowercase alphabetic character has been flipped to uppercase and each uppercase alphabetic character has been flipped to lowercase, while non-alphabetic characters remain unchanged. This is achieved through the use of a list comprehension and the `swapcase()` method for individual characters.

Here's an example usage of the `flip_case` function with the input argument **"Hello, World!"**:
```python
print(flip_case("Hello, World!"))  # Output: "hELLO, wORLD!"
```

This will produce the output "hELLO, wORLD!" with all alphabetic characters flipped accordingly. 

The script successfully addresses the challenge of flipping the case of alphabetic characters within a given string, while leaving non-alphabetic characters unaffected.