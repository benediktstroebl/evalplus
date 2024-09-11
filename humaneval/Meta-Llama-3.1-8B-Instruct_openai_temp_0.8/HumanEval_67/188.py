```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number of fruits, 
    and the number of apples and oranges.

    Args:
        s (str): A string that represents the total number of oranges and apples.
        n (int): An integer that represents the total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """

    # Use regular expression to extract the total number of apples and oranges from the string
    apples, oranges = map(int, re.findall(r'\d+', s))

    # Calculate the total number of apples and oranges
    total_fruits_without_mango = apples + oranges

    # Return the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits
    return n - total_fruits_without_mango

# Test the function with example inputs
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))    # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script defines a function `fruit_distribution` that takes a string `s` and an integer `n` as input, extracts the total number of apples and oranges from `s` using regular expressions, calculates the total number of apples and oranges, and returns the number of mango fruits by subtracting the total number of apples and oranges from `n`. The script then tests the function with example inputs.