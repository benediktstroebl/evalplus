```python
import re

def fruit_distribution(s, n):
    """
    Calculates the number of mango fruits in the basket.

    Args:
        s (str): A string representing the total number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.

    Examples:
        >>> fruit_distribution("5 apples and 6 oranges", 19)
        8
        >>> fruit_distribution("0 apples and 1 oranges", 3)
        2
        >>> fruit_distribution("2 apples and 3 oranges", 100)
        95
        >>> fruit_distribution("100 apples and 1 oranges", 120)
        19
    """
    # Use regular expression to extract the number of apples and oranges
    match = re.search(r"(\d+) apples and (\d+) oranges", s)
    if match:
        # Convert the extracted numbers to integers
        apples = int(match.group(1))
        oranges = int(match.group(2))
        # Calculate the number of mangoes
        mangoes = n - apples - oranges
        return mangoes
    else:
        # If the input string does not match the expected pattern, return -1
        return -1

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```