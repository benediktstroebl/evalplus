```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits, 
    apples, and oranges.

    Args:
        s (str): A string representing the number of apples and oranges.
        n (int): The total number of fruits in the basket.

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
    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r'(\d+) apples and (\d+) oranges', s)
    
    # If the string matches the pattern, extract the numbers
    if match:
        apples, oranges = map(int, match.groups())
    # If the string does not match the pattern, try to extract the numbers as a single value
    else:
        match = re.search(r'(\d+)', s)
        if match:
            total = int(match.group())
            return n - total
        else:
            raise ValueError("Invalid input string")

    # Return the number of mango fruits
    return n - apples - oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # 19
```

This script uses a regular expression to extract the numbers of apples and oranges from the input string. If the string does not match the expected pattern, it tries to extract the numbers as a single value. The function then returns the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits in the basket.