### Fruit Distribution Calculator
```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits and 
    the distribution of apples and oranges.

    Args:
        s (str): A string representing the total number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Regular expression to extract the number of apples and oranges from the string
    match = re.search(r"(\d+) apples and (\d+) oranges", s)
    
    if match:
        apples = int(match.group(1))
        oranges = int(match.group(2))
        return n - apples - oranges
    else:
        return "Invalid input format"

# Example use cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses regular expressions to extract the number of apples and oranges from the input string. The extracted numbers are then subtracted from the total number of fruits to calculate the number of mangoes. If the input string does not match the expected format, the function returns an error message.