```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number of fruits,
    the number of apples, and the number of oranges.
    
    Parameters:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.
    
    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to find the number of apples and oranges in the string
    apples = int(re.search(r'\d+(?= apples)', s).group())
    oranges = int(re.search(r'\d+(?= oranges)', s).group())
    
    # Calculate the total number of apples and oranges
    total_fruits = apples + oranges
    
    # Return the number of mango fruits
    return n - total_fruits

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))   # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))    # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))# Output: 19
```

This script uses a regular expression to find the number of apples and oranges in the given string. It then calculates the total number of fruits and returns the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits.