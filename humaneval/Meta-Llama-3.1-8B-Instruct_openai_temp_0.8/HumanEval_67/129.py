```python
import re

def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in the basket.

    Args:
    s (str): A string that represents a number of apples and oranges.
    n (int): The total number of the fruits in the basket.

    Returns:
    int: The number of the mango fruits in the basket.
    """
    # Use regular expression to extract numbers from the string
    numbers = re.findall(r'\d+', s)
    
    # Convert extracted numbers to integers
    apples = int(numbers[0])
    oranges = int(numbers[2])
    
    # Calculate the number of mango fruits
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses regular expressions to extract the numbers of apples and oranges from the input string. It then calculates the number of mango fruits by subtracting the numbers of apples and oranges from the total number of fruits.