```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script defines a function `flip_case` that takes a string as an input and returns a string with flipped case, ensuring that non-alphabetic characters remain unchanged. This approach utilizes the `swapcase()` method for alphabetic characters and retains non-alphabetic characters as is. 

The `swapcase()` method is applied to alphabetic characters, which swaps the case of each character. This means that if a character is in uppercase, it is changed to lowercase, and vice versa. The `join()` method is used to concatenate the characters with their new case and the non-alphabetic characters that remain unchanged. 

This approach ensures that the function is self-contained and provides a simple, efficient solution to the problem. 
The `flip_case` function can be called directly with a string as an argument to see its behavior: `print(flip_case('hello, world!'))`. 

This would output: 
`hELLO, wORLD!`

The exclamation mark and comma were not affected by the flip since they are non-alphabetic characters.