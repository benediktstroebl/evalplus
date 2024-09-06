```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script defines a function that flips the case of alphabetic characters in a string, swapping uppercase to lowercase and vice versa. It uses a list comprehension to iterate through each character in the input string. For alphabetic characters, it employs the `swapcase()` method to flip their case. Non-alphabetic characters like punctuation are left unchanged. The final output is returned as a string, where the case of alphabetic characters has been flipped appropriately.

Here's an example usage of this function:
```python
print(flip_case("Hello, World!"))
```

Output:
```
hELLO, wORLD!
```