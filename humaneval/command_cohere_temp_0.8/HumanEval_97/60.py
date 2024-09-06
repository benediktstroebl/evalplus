```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputs."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The Python script defines a function `multiply(a, b)` that takes two integer inputs `a` and `b`, extracts the last digit of each number using `int(str(number)[-1])`, and returns the product of these extracted digits, thereby accomplishing the task as outlined in the problem statement. This straightforward approach leverages string manipulation and integer conversion to efficiently determine the product of the unit digits.