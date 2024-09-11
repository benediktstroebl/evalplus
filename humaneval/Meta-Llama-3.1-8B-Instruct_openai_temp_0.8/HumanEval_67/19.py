```python
import re

def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in a basket given a string representing the number of apples and oranges, 
    and an integer representing the total number of fruits.

    Args:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r"(\d+) apples and (\d+) oranges", s)
    
    # If the string matches the pattern, extract the numbers and calculate the number of mangoes
    if match:
        num_apples = int(match.group(1))
        num_oranges = int(match.group(2))
        return n - num_apples - num_oranges
    else:
        # If the string does not match the pattern, raise a ValueError
        raise ValueError("Invalid input string. It should be in the format 'X apples and Y oranges'.")

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script defines a function `fruit_distribution` that takes a string `s` and an integer `n` as input. It uses regular expression to extract the numbers of apples and oranges from the string, and then calculates the number of mangoes by subtracting the numbers of apples and oranges from the total number of fruits `n`. If the input string does not match the expected pattern, it raises a `ValueError`.