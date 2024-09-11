```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Parameters:
    s (str): A string that represents the total number of apples and oranges.
    n (int): An integer that represents the total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r"(\d+) apples and (\d+) oranges", s)
    if match:
        apples, oranges = map(int, match.groups())
    else:
        raise ValueError("Invalid input string")

    # Return the total number of fruits minus the numbers of apples and oranges
    return n - apples - oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script uses the `re` module to extract the numbers of apples and oranges from the input string using a regular expression. It then calculates and returns the number of mango fruits by subtracting the numbers of apples and oranges from the total number of fruits. If the input string is invalid, it raises a `ValueError`.