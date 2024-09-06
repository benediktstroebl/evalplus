```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() for char in string)
```
The function uses a list comprehension with a `swapcase` iterator to flip the case of each character in the string. This method is more efficient as it requires fewer operations and avoids creating multiple variables. Thus, it improves code readability and maintains the problem-solving efficiency.