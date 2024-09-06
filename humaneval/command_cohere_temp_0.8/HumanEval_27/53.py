```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() for char in string)
```
The function directly uses the `swapcase()` method, which saves the need for an explicit loop and char mapping, making the code more efficient and concise.