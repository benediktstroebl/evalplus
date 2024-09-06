```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses a list comprehension with a conditional statement to determine whether each character of the input string should be flipped case-wise. The `isalpha()` method checks if each character is alphabetic, and the `swapcase()` method is used to swap the case of the character if it is. Meanwhile, non-alphabetic characters like punctuation are left unchanged. The final output is achieved by joining the list of modified characters back into a string. 

The code ensures that all characters are appropriately manipulated based on their alphabetic nature, enhancing the clarity and correctness of the solution.