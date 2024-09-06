```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputs."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The Python function `multiply(a, b)` takes two integers as input and returns the product of their unit digits. It does so by extracting the last digit using `str(a)[-1]` and `str(b)[-1]`, converting them to integers (`int()`), and then multiplying them together. 

Here is an example of usage:
```python
print(multiply(12, 3))
```
Should return 4, as the unit digits of 12 and 3 are 2 and 3, respectively, and their product is 6 (written as `2 * 3`).