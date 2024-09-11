```python
import re

def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Args:
        s (str): A string that represents the total number of the oranges and apples and 
                 their quantities in the basket.
        n (int): An integer that represents the total number of the fruits in the basket.

    Returns:
        int: The number of the mango fruits in the basket.
    """
    # Use regular expression to find the number of apples and oranges in the string
    apples = int(re.search(r'\d+ apples', s).group().split(' ')[0])
    oranges = int(re.search(r'\d+ oranges', s).group().split(' ')[0])

    # Return the difference between the total number and the number of apples and oranges
    return n - apples - oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19)) # -> 8
print(fruit_distribution("0 apples and 1 oranges", 3)) # -> 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # -> 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # -> 19
```
This Python script uses regular expressions to find the number of apples and oranges in the given string, and then returns the difference between the total number of fruits and the sum of apples and oranges.