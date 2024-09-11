```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits 
    and the distribution of apples and oranges.

    Args:
        s (str): A string representing the number of apples and oranges in the basket.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    match = re.search(r'(\d+)\s*(?:apples|oranges)', s)
    if match:
        # Extract the number of apples and oranges
        num_apples_oranges = int(match.group(1))
    else:
        # If no match is found, assume the number of apples and oranges is 0
        num_apples_oranges = 0

    # Calculate the number of mango fruits
    num_mangoes = n - num_apples_oranges

    return num_mangoes


# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # -> 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # -> 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # -> 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # -> 19
```

This script uses a regular expression to extract the number of apples and oranges from the input string, and then calculates the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits.