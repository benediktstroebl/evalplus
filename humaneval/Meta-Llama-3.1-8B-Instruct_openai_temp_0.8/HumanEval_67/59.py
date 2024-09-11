```python
import re

def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in a basket given a string representing the total 
    number of apples and oranges, and the total number of fruits in the basket.

    Args:
        s (str): A string representing the total number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the total number of apples and oranges
    total_fruits = apples + oranges
    
    # Return the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits
    return n - total_fruits

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses the `re` module's `findall` function to extract the numbers from the input string using a regular expression. It then converts these numbers to integers and calculates the total number of fruits by adding the number of apples and oranges. Finally, it returns the number of mango fruits by subtracting the total number of fruits from the total number of fruits in the basket.