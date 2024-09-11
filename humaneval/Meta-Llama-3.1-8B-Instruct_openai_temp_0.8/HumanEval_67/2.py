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
        s (str): A string representing the total number of oranges and apples.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    
    # Regular expression pattern to match the numbers of apples and oranges
    pattern = r"(\d+) apples and (\d+) oranges"
    
    # Search for the pattern in the string
    match = re.search(pattern, s)
    
    # If the pattern is found, extract the numbers of apples and oranges
    if match:
        apples = int(match.group(1))
        oranges = int(match.group(2))
        
        # Return the number of mango fruits
        return n - apples - oranges
    else:
        # If the pattern is not found, raise a ValueError
        raise ValueError("Invalid input string")

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # 19
```

This script uses a regular expression to search for the numbers of apples and oranges in the input string. If the pattern is found, it extracts the numbers and returns the number of mango fruits by subtracting the numbers of apples and oranges from the total number of fruits. If the pattern is not found, it raises a ValueError.