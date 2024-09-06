```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputs."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments. It extracts the last digit of each number by accessing the last element of their string representations using `str(a)[-1]` and `str(b)[-1]`. These are converted back to integers using `int()` to multiply them together. The result is then returned as the product of the unit digits. 

Here is an example usage of the function:
```python
print(multiply(12, 3))
```
This would output:
```
6
```