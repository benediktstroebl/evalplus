```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return bool(a or b or c)
```

This function checks if any combination of adding two of the three numbers equals the third number. 

The function returns `true` if any of these conditions are met, indicating that one of the numbers is equal to the sum of the other two.

This problem can be solved through thinking about the intuition behind the idea and testing cases that match the sum of two numbers as well as border cases to ensure correctness.

This script solves the problem in a concise manner while still remaining readable and adhering to Python best practices.

For more complex problems or coding concepts, feel free to ask for assistance!