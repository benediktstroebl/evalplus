```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as input and returns a new string where the case of letters has been flipped, excluding non-alphabetic characters. Here's a step-by-step breakdown:
1. The `def flip_case(string: str) -> str:` function definition specifies that this function takes a string as input and returns a string.
2. The function is implemented using a list comprehension with a condition for character case flipping. It iterates through each character in the input string.
3. For alphabetic characters, the `swapcase()` function is applied, which swaps the case of the character (e.g., 'H' becomes 'h'). For non-alphabetic characters, the original character remains unchanged.
4. The resulting string with flipped letters and unchanged non-letter characters is then joined back together to form the final output string.

This solution is concise and achieves the intended functionality while maintaining a self-contained code block that is easy to understand.