```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function leverages string manipulation to capture and multiply the unit digits of the two input numbers, providing an efficient solution. It's concise yet intuitive and achieves the stated goal.