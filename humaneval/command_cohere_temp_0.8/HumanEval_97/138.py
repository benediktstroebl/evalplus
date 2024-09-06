```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputs."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The Python script defines a function `multiply(a, b)` that takes two integer inputs `a` and `b` and returns the product of the unit digits of `a` and `b`. The function achieves this by extracting the last digit using `str(a)[-1]` and `str(b)[-1]` in conjunction with the `int()` function to convert it back to an integer. 

This solution directly targets the asked problem, extracting the unit digits and multiplying them, whereas alternative solutions may be overkill in terms of functionality.