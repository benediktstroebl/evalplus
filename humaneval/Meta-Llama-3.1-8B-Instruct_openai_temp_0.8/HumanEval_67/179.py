```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket.
    
    Parameters:
    s (str): A string that represents the total number of apples and oranges.
    n (int): The total number of fruits in the basket.
    
    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Regular expression pattern to match numbers and fruits
    pattern = r"(\d+)\s*(apples|oranges)"
    
    # Use the regular expression to find numbers and fruits in the string
    matches = re.findall(pattern, s)
    
    # Initialize total apples and oranges to 0
    total_apples = 0
    total_oranges = 0
    
    # Loop through the matches and calculate the total apples and oranges
    for match in matches:
        number = int(match[0])
        fruit = match[1]
        if fruit == "apples":
            total_apples += number
        elif fruit == "oranges":
            total_oranges += number
    
    # Return the total number of fruits minus the total apples and oranges
    return n - total_apples - total_oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script uses the `re` module to find numbers and fruits in the input string. It then loops through the matches to calculate the total number of apples and oranges. Finally, it returns the total number of fruits minus the total apples and oranges.