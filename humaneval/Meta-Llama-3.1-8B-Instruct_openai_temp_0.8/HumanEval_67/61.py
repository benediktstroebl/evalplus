```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Args:
        s (str): A string representing the total number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges
    match = re.search(r'(\d+) apples and (\d+) oranges', s)
    if match:
        apples = int(match.group(1))
        oranges = int(match.group(2))
        # Return the total number of fruits minus the number of apples and oranges
        return n - apples - oranges
    else:
        # If the string format is incorrect, raise an exception
        raise ValueError("Invalid input format")

# Example usage:
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script uses regular expressions to extract the numbers of apples and oranges from the input string. It then subtracts these numbers from the total count of fruits in the basket to calculate the number of mango fruits. The example usage at the end shows how to use the `fruit_distribution` function with different inputs.