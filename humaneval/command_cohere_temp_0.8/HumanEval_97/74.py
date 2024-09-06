```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputs."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The Python script defines a function `multiply(a, b)` that takes two integer inputs `a` and `b` and returns the product of the unit digits of `a` and `b`. The function achieves this by extracting the last digit using `str(a)[-1]` and `str(b)[-1]`. The over-all complexity of this solution is O(1).