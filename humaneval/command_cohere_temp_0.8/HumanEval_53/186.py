```python
def add(x: int, y: int):
    return x + y
```
The function takes in two arguments, x and y, both of type integer, and it returns the result of adding the two values. 

To verify the functionality, you can add tests that validate the addition of different numbers, as shown below:
```python
# Test the function with different inputs
assert add(2, 3) == 5
assert add(5, 7) == 12
assert add(0, 0) == 0
assert add(10, 2) == 12
```