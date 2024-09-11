### Fruit Distribution Problem Solution
```python
import re

def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Parameters:
    s (str): A string that represents a number of apples and oranges in a basket.
    n (int): An integer that represent the total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.

    Examples:
    >>> fruit_distribution("5 apples and 6 oranges", 19)
    8
    >>> fruit_distribution("0 apples and 1 oranges", 3)
    2
    >>> fruit_distribution("2 apples and 3 oranges", 100)
    95
    >>> fruit_distribution("100 apples and 1 oranges", 120)
    19
    """
    # Use regular expression to extract numbers from the string
    numbers = list(map(int, re.findall(r'\d+', s)))
    
    # Extract the numbers of apples and oranges
    apples, oranges = numbers[0], numbers[1]
    
    # Calculate the number of mango fruits
    mango = n - apples - oranges
    
    return mango

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```
This script defines a function `fruit_distribution` that takes a string `s` representing the total number of apples and oranges, and an integer `n` representing the total number of fruits in the basket. It uses regular expression to extract the numbers of apples and oranges from the string, and then calculates the number of mango fruits by subtracting the numbers of apples and oranges from the total number of fruits. The function returns the number of mango fruits.