### Fruit Distribution Script
```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits and the number of apples and oranges.

    Args:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    match = re.search(r"(\d+) apples and (\d+) oranges", s)
    if match:
        num_apples, num_oranges = map(int, match.groups())
        # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total
        return n - num_apples - num_oranges
    else:
        # If the string does not match the expected format, raise an exception
        raise ValueError("Invalid input string")

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```
This script defines a function `fruit_distribution` that takes a string `s` and an integer `n` as input. It uses regular expressions to extract the number of apples and oranges from the string, and then calculates the number of mango fruits by subtracting the number of apples and oranges from the total. The function includes error handling to raise a `ValueError` if the input string does not match the expected format.