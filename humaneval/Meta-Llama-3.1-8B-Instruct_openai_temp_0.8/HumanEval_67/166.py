```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the string representation of apples and oranges, and the total number of fruits.

    Args:
        s (str): A string representing the total number of apples and oranges in the basket.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """

    # Use regular expression to extract the numbers of apples and oranges from the string
    apples, oranges = map(int, re.findall(r'\d+', s))

    # Calculate the total number of apples and oranges
    total_fruits = apples + oranges

    # Return the number of mango fruits, which is the difference between the total number of fruits and the total number of apples and oranges
    return n - total_fruits

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses a regular expression to extract the numbers of apples and oranges from the input string. It then calculates the total number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits.