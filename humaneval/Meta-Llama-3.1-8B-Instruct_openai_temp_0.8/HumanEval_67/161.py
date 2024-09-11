```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number of fruits, 
    apples and oranges.

    Parameters:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    match = re.search(r"(\d+) apples and (\d+) oranges", s)
    
    if match:
        apples = int(match.group(1))
        oranges = int(match.group(2))
        
        # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total
        mangoes = n - apples - oranges
        
        return mangoes
    else:
        # If the input string does not match the expected pattern, return an error message
        return "Invalid input format"

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This Python script defines a function `fruit_distribution` that takes a string `s` and an integer `n` as input. It uses regular expressions to extract the number of apples and oranges from the string, calculates the number of mango fruits by subtracting the number of apples and oranges from the total, and returns the result. The script also includes test cases to demonstrate the function's usage.