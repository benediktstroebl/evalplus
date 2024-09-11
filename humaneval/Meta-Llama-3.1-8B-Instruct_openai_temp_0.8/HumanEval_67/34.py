```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Parameters:
    s (str): A string that represents the total number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers of apples and oranges from the string
    numbers = re.findall(r'\d+', s)
    
    # Convert the extracted numbers to integers and sum them up
    total_fruits = sum(map(int, numbers))
    
    # Subtract the total fruits (apples and oranges) from the total number of fruits in the basket
    mangoes = n - total_fruits
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses a regular expression to extract the numbers from the input string, assuming that the numbers are separated by spaces and words (like "apples and"). It then subtracts the sum of these numbers from the total number of fruits in the basket to get the number of mangoes.