```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits, 
    apples, and oranges.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to find the total number of apples and oranges in the string
    total_fruit = re.findall(r'\d+', s)
    
    # Check if the string contains both apples and oranges
    if len(total_fruit)!= 2:
        raise ValueError("Invalid input string. It must contain both apples and oranges.")
    
    # Convert the strings to integers
    apples = int(total_fruit[0])
    oranges = int(total_fruit[1].replace(' oranges', ''))
    
    # Calculate the number of mango fruits
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))# Output: 19
```

This script uses a regular expression to find the total number of apples and oranges in the input string. It then calculates the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits. The function includes input validation to check if the string contains both apples and oranges.