```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number of fruits, 
    oranges, and apples.

    Parameters:
    s (str): A string representing the total number of oranges and apples.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the number of apples and oranges from the string
    match = re.search(r"(\d+) apples and (\d+) oranges", s)
    
    # If the string matches the pattern, extract the numbers
    if match:
        apples, oranges = match.groups()
    else:
        raise ValueError("Invalid input string. Please use the format 'x apples and y oranges'")

    # Convert the extracted numbers to integers
    apples, oranges = int(apples), int(oranges)

    # Calculate the number of mango fruits
    mangoes = n - apples - oranges

    return mangoes

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script defines a function `fruit_distribution` that takes a string `s` and an integer `n` as input. It uses regular expressions to extract the number of apples and oranges from the string, then calculates the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits.