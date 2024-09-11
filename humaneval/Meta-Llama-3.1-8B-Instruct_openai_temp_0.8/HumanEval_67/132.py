```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits,
    apples, and oranges.

    Parameters:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    matches = re.findall(r"(\d*)\s*(oranges|apples)", s)
    
    # Initialize variables to store the number of apples and oranges
    oranges = 0
    apples = 0

    # Parse the extracted matches and update the number of apples and oranges
    for match in matches:
        if match[1] == "oranges":
            oranges = int(match[0]) if match[0] else 0
        elif match[1] == "apples":
            apples = int(match[0]) if match[0] else 0

    # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total
    return n - apples - oranges

# Test the function with example inputs
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses regular expressions to extract the number of apples and oranges from the input string. It then calculates the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits.