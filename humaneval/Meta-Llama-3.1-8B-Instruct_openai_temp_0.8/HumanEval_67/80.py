```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given a string representing the total number of apples and oranges and an integer representing the total number of fruits.

    Args:
        s (str): A string that represents a number of apples and oranges in a basket.
        n (int): An integer that represents the total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers of apples and oranges from the string
    numbers = re.findall(r'\d+', s)
    
    # Convert the extracted numbers to integers
    apples = int(numbers[0])
    oranges = int(numbers[1])
    
    # Calculate the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script uses the `re` module's `findall` function to extract the numbers from the input string using a regular expression. It then converts these numbers to integers and calculates the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits.