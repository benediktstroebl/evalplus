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
    s (str): a string that represents the total number of the oranges and apples
    n (int): an integer that represent the total number of the fruits in the basket

    Returns:
    int: the number of the mango fruits in the basket
    """
    
    # Use regular expression to find all numbers in the string
    numbers = list(map(int, re.findall(r'\d+', s)))
    
    # The first number is the total number of apples and oranges, the second number is the total number of oranges
    apples_and_oranges = numbers[0]
    oranges = numbers[1]
    
    # The total number of apples and oranges is the sum of apples and oranges
    apples = apples_and_oranges - oranges
    
    # Return the number of mango fruits, which is the total number of fruits minus the number of apples and oranges
    return n - apples - oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19)) # 8
print(fruit_distribution("0 apples and 1 oranges", 3)) # 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # 19
```