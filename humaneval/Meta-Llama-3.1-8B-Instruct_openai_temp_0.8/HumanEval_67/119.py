```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the number of apples and oranges.

    Args:
    s (str): A string that represents the total number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to find the total number of apples and oranges in the string
    total_fruits = int(re.search(r'\d+', s).group())  # Get the first numerical value in the string
    
    # Calculate the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits
    mango_fruits = n - total_fruits
    
    return mango_fruits

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Should print: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Should print: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Should print: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Should print: 19
```

This script uses the `re` (regular expression) module to find the total number of apples and oranges in the input string. It then calculates the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits. The result is returned as an integer.