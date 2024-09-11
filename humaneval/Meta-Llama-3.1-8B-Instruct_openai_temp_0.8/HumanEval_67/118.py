```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given a string that represents 
    the total number of apples and oranges and an integer that represents the total 
    number of fruits in the basket.

    Args:
    s (str): A string that represents the total number of apples and oranges.
    n (int): An integer that represents the total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    matches = re.findall(r'\d+', s)
    
    # Convert the matches to integers
    apples = int(matches[0])
    oranges = int(matches[1])
    
    # Calculate the total number of apples and oranges
    total_fruit = apples + oranges
    
    # Return the difference between the total number of fruits and the total number of apples and oranges
    return n - total_fruit

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses a regular expression to extract the numbers of apples and oranges from the input string, converts them to integers, calculates the total number of apples and oranges, and returns the difference between the total number of fruits and the total number of apples and oranges.