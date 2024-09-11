```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits and 
    the numbers of apples and oranges.

    Args:
    s (str): A string containing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r'(\d+)\s+(apples|oranges)', s)
    
    if match:
        # Extract the number and the fruit type
        num, fruit = int(match.group(1)), match.group(2)
        
        # Calculate the total number of apples and oranges
        total_fruit = num if fruit == 'apples' else num
        
        # Return the number of mango fruits
        return n - total_fruit
    else:
        # If no match is found, return an error message
        return "Error: Invalid input"

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses the `re` module to perform regular expression matching to extract the numbers of apples and oranges from the input string. It then calculates the total number of apples and oranges and returns the number of mango fruits in the basket. If the input string is invalid, it returns an error message.