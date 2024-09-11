```python
import re

def fruit_distribution(fruits, total):
    """
    Calculate the number of mango fruits in a basket.

    Args:
        fruits (str): A string representing the total number of apples and oranges.
        total (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.

    Example:
        >>> fruit_distribution("5 apples and 6 oranges", 19)
        8
        >>> fruit_distribution("0 apples and 1 oranges", 3)
        2
        >>> fruit_distribution("2 apples and 3 oranges", 100)
        95
        >>> fruit_distribution("100 apples and 1 oranges", 120)
        19
    """

    # Use regular expression to extract the numbers of apples and oranges
    match = re.search(r'(\d+)\s+apples\s+and\s+(\d+)\s+oranges', fruits)

    # Extract the numbers of apples and oranges from the match
    if match:
        apples = int(match.group(1))
        oranges = int(match.group(2))

        # Calculate the number of mango fruits
        return total - apples - oranges
    else:
        # If the input string does not match the expected format, return an error message
        return "Invalid input format"

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Outputs: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Outputs: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Outputs: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Outputs: 19
```

This script uses the `re` module to extract the numbers of apples and oranges from the input string using a regular expression. It then calculates the number of mango fruits by subtracting the numbers of apples and oranges from the total number of fruits. If the input string does not match the expected format, it returns an error message.