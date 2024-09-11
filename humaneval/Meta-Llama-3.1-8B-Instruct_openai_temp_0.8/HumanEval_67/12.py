```python
import re

def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in the basket by subtracting the total number of apples and oranges from the total number of fruits.

    Args:
        s (str): A string that represents the total number of the oranges and apples.
        n (int): An integer that represents the total number of the fruits in the basket.

    Returns:
        int: The number of the mango fruits in the basket.
    """
    
    # Use regular expression to extract the total number of apples and oranges from the string
    apples = int(re.search(r'\d+(?= apples)', s).group())
    oranges = int(re.search(r'\d+(?= oranges)', s).group())
    
    # Calculate the total number of mangoes by subtracting the total number of apples and oranges from the total number of fruits
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses a regular expression to extract the total number of apples and oranges from the input string. It then calculates the total number of mangoes by subtracting the total number of apples and oranges from the total number of fruits. The result is returned as an integer.