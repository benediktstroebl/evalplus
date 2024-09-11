```python
import re

def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in a basket given a string of fruit counts
    and the total number of fruits.

    Parameters:
    s (str): A string containing the counts of apples and oranges.
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
    # Use regular expression to extract the counts of apples and oranges
    counts = re.findall(r"(\d+) (apples|oranges)", s)
    
    # Initialize the counts of apples and oranges to 0
    apples, oranges = 0, 0
    
    # Extract the counts of apples and oranges from the list of tuples
    for count, fruit in counts:
        if fruit == "apples":
            apples = int(count)
        elif fruit == "oranges":
            oranges = int(count)
    
    # Return the total number of fruits minus the counts of apples and oranges
    return n - apples - oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```