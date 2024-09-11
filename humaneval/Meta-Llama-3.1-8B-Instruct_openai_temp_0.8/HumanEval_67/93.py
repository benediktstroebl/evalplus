```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits, 
    and the number of apples and oranges.

    Args:
        s (str): A string that represents the number of apples and oranges in the basket.
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
    # Use regular expression to find the number of apples and oranges
    matches = re.findall(r'(\d+) apples and (\d+) oranges', s)
    
    if matches:
        # Extract the number of apples and oranges from the matches
        apples, oranges = map(int, matches[0])
        # Calculate the number of mango fruits
        return n - apples - oranges
    else:
        # If the input string does not match the expected format, return an error message
        return "Invalid input string"

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # 19
```