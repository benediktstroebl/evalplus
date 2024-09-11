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
        s (str): A string that represents the total number of the oranges and apples.
        n (int): An integer that represent the total number of the fruits in the basket.

    Returns:
        int: The number of the mango fruits in the basket.
    """
    
    # Use regular expression to find the numbers of apples and oranges in the string
    numbers = re.findall(r'\d+', s)
    
    # Convert the found numbers to integers
    apples = int(numbers[0])
    oranges = int(numbers[1])
    
    # Calculate the number of mango fruits
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function with example inputs
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script defines a function `fruit_distribution` that takes two parameters: a string `s` representing the distribution of apples and oranges, and an integer `n` representing the total number of fruits in the basket. It uses regular expression to find the numbers of apples and oranges in the string, calculates the number of mango fruits by subtracting the numbers of apples and oranges from the total number of fruits, and returns the result. The script also includes test cases to demonstrate the function's behavior.