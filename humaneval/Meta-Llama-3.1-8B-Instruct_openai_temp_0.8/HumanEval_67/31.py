```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Args:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    apples_oranges = re.findall(r'(\d+) apples? and (\d+) oranges?', s)
    
    # If no matches are found, return an error message
    if not apples_oranges:
        return "Error: Unable to extract number of apples and oranges."
    
    # Extract the numbers of apples and oranges from the match
    apples, oranges = map(int, apples_oranges[0])
    
    # Calculate the number of mango fruits
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses a regular expression to extract the numbers of apples and oranges from the input string, and then calculates the number of mango fruits by subtracting these numbers from the total number of fruits in the basket. If no matches are found in the input string, the function returns an error message.