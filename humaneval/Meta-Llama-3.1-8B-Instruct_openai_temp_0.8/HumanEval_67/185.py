```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the distribution of apples and oranges.

    Args:
        s (str): A string representing the total number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses the `re` module to extract the numbers from the string using regular expressions. The `findall` method returns a list of all non-overlapping matches of the regular expression in the string as strings. The `map` function is then used to convert the extracted numbers to integers. The number of mango fruits is finally calculated by subtracting the number of apples and oranges from the total number of fruits.