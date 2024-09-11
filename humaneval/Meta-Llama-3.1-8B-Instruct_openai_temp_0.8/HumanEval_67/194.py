```python
import re

def fruit_distribution(s, total_fruits):
    """
    This function calculates the number of mango fruits in a basket given the total number of fruits, 
    apples and oranges.

    Parameters:
    s (str): A string that represents the total number of apples and oranges in the basket.
    total_fruits (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r"(\d+) apples and (\d+) oranges", s)
    
    # If the string matches the pattern, extract the numbers
    if match:
        num_apples = int(match.group(1))
        num_oranges = int(match.group(2))
        
        # Calculate the number of mango fruits
        num_mango = total_fruits - num_apples - num_oranges
        
        return num_mango
    
    # If the string does not match the pattern, return an error message
    else:
        return "Failed to parse input string"

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses the `re` module to extract the numbers of apples and oranges from the input string using a regular expression. It then calculates the number of mango fruits by subtracting the numbers of apples and oranges from the total number of fruits.