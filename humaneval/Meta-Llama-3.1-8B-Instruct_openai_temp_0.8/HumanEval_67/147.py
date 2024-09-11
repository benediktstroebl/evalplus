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
    s (str): A string that contains the number and type of apples and oranges
    n (int): The total number of fruits in the basket

    Returns:
    int: The number of mango fruits in the basket
    """

    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r'(\d+)\s+apples\s+and\s+(\d+)\s+oranges', s)
    
    if match:
        # Extract the numbers of apples and oranges from the match
        apples, oranges = int(match.group(1)), int(match.group(2))
        
        # Return the number of mango fruits in the basket
        return n - apples - oranges
    else:
        # If the input string does not match the expected pattern, return an error message
        return "Invalid input string"

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19)) # -> 8
print(fruit_distribution("0 apples and 1 oranges", 3)) # -> 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # -> 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # -> 19
```

This script defines a function `fruit_distribution` that takes two parameters: `s` (a string containing the number and type of apples and oranges) and `n` (the total number of fruits in the basket). It uses a regular expression to extract the numbers of apples and oranges from the string, and then returns the number of mango fruits in the basket by subtracting the numbers of apples and oranges from the total number of fruits.