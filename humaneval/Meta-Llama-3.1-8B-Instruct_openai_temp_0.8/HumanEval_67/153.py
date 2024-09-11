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
    s (str): A string that represents a number of apples and oranges 
             that are distributed in a basket of fruit
    n (int): An integer that represent the total number of the fruits in the basket

    Returns:
    int: The number of the mango fruits in the basket
    """
    # Use regular expression to find numbers in the string
    nums = list(map(int, re.findall(r'\d+', s)))
    
    # Calculate the number of apples and oranges
    apples = nums[0]
    oranges = nums[1]
    
    # Return the number of mango fruits
    return n - apples - oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses the `re.findall` function to find all numbers in the input string `s`. The `map` function is then used to convert these numbers to integers. The numbers of apples and oranges are extracted from the list of numbers, and the number of mango fruits is calculated by subtracting the numbers of apples and oranges from the total number of fruits `n`.