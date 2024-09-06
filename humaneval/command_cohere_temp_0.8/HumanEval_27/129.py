```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert alphabetic characters to their flip case counterparts, while leaving non-alphabetic characters unchanged. It leverages Python's str.swapcase() method, which swaps the case of letters: lowercase becomes uppercase and vice versa. A list comprehension is employed to iterate through each character in the input string. For alphabetic characters, the swapcase() function is applied, while non-alphabetic characters like punctuation are retained in their original form. The final result is a string with the desired flip case transformation.