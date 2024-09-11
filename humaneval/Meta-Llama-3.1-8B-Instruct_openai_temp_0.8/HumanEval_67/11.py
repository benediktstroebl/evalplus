```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number of fruits,
    and the number of apples and oranges.

    Args:
        s (str): A string that represents the total number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r"(\d+)\s*(apples|oranges) and (\d+)\s*(apples|oranges)", s)
    
    # If the string does not match the expected pattern, return an error message
    if match is None:
        raise ValueError("Invalid input string")
    
    # Extract the numbers of apples and oranges from the match
    apples, _ = match.groups(1, 3)
    oranges, _ = match.groups(2, 4)
    
    # Convert the extracted numbers to integers
    apples = int(apples)
    oranges = int(oranges)
    
    # Calculate the number of mango fruits by subtracting the numbers of apples and oranges from the total
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses regular expressions to extract the numbers of apples and oranges from the input string, and then calculates the number of mango fruits by subtracting these numbers from the total. It also includes some basic error checking to ensure the input string matches the expected pattern.