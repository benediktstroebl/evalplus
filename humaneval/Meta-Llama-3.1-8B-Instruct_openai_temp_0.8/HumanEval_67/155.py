```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given a string 
    representing the total number of apples and oranges and an integer representing 
    the total number of fruits in the basket.

    Args:
    s (str): A string representing the total number of apples and oranges.
    n (int): An integer representing the total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expressions to extract the number of apples and oranges from the string
    apples = int(re.search(r'\d+(?= apples)', s).group())
    oranges = int(re.search(r'\d+(?= oranges)', s).group())
    
    # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total
    return n - apples - oranges

# Test the function with the provided examples
print(fruit_distribution("5 apples and 6 oranges", 19))   # 8
print(fruit_distribution("0 apples and 1 oranges", 3))    # 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # 19
```

This script uses regular expressions to extract the number of apples and oranges from the input string, and then calculates the number of mango fruits by subtracting these numbers from the total number of fruits. The result is then returned by the function.