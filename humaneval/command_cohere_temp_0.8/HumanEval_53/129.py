```python
def add(x: int, y: int):
    """
    Add two numbers x and y
    Returns:
        int: Sum of x and y
    """
    return x + y
```
The function signature, `x: int` and `y: int`, shows the expected input types are integers. The `Returns` clause of the docstring informs users about the return value, appropriately updated accordingly.

Here is an example of how to use this function:
```python
result = add(2, 3)
print(result)
```
```
5
```
And another example:
```python
result = add(5, 7)
print(result)
```
```
12
```
These examples demonstrate the function's ability to add any two given integers, updating the docstring to be accurate and informative.