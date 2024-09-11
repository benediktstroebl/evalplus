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
        s (str): A string that represents the total number of apples and oranges.
        n (int): An integer that represents the total number of the fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r"(\d+)\s*apples?\s*and\s*(\d+)\s*oranges?", s)
    if match:
        apples = int(match.group(1))
        oranges = int(match.group(2))
        # Return the difference between the total number of fruits and the number of apples and oranges
        return n - apples - oranges
    else:
        # If the string does not match the expected pattern, return an error message
        return "Invalid input string"

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses a regular expression to extract the numbers of apples and oranges from the input string. It then returns the difference between the total number of fruits and the number of apples and oranges. If the input string does not match the expected pattern, it returns an error message.