```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expressions to extract numbers from the string
    numbers = list(map(int, re.findall(r'\d+', s)))
    
    # Check if the string contains "apples" and "oranges"
    if "apples" not in s or "oranges" not in s:
        return "Invalid string format"
    
    # Calculate the number of mango fruits
    return n - sum(numbers[:2])

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 4
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script uses regular expressions to extract the numbers from the input string, and then subtracts the total number of apples and oranges from the total number of fruits to get the number of mango fruits. If the string does not contain "apples" and "oranges", it returns an error message.