```python
import re

def fruit_distribution(s, n):
    """
    Calculates the number of mango fruits in a basket given the total number of fruits,
    apples, and oranges.

    Args:
        s (str): A string representing the total number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r"(\d+)\s*(apples|oranges)", s)
    
    if match:
        # Extract the numbers and convert them to integers
        num_fruit, fruit_type = match.groups()
        num_fruit = int(num_fruit)
        
        # Calculate the total number of fruits that are not mangoes
        total_non_mango = num_fruit
        
        # Check if the total number of non-mango fruits matches the string
        if fruit_type == "oranges":
            total_non_mango += num_fruit
        
        # Return the number of mango fruits
        return n - total_non_mango
    else:
        # If the string does not match the expected format, return an error message
        return "Invalid input format"

# Test the function with examples
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script uses a regular expression to extract the numbers of apples and oranges from the input string. It then calculates the total number of non-mango fruits and returns the number of mango fruits by subtracting this total from the total number of fruits in the basket. If the input string does not match the expected format, the function returns an error message.