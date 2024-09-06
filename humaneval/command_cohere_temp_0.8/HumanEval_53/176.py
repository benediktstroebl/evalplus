```python
def add(x: int, y: int):
    return x + y
```
The function takes in two arguments, both integers, and returns their sum. 

To further specify this in the comments, you could add examples of tests that can be done to ensure it is functioning properly. These can be added to the function documentation as follows:
```python
def add(x: int, y: int):
    """
    Add two numbers x and y
    
    Tests:
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    >>> add(10, -3)
    7
    >>> add(-5, 5)
    0
    """
    return x + y
```