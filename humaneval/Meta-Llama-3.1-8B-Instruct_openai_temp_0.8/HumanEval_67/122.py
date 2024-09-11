```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the distribution of apples and oranges.

    Args:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    matches = re.findall(r'\d+', s)
    
    # Convert the extracted numbers to integers
    num_apples = int(matches[0])
    num_oranges = int(matches[1])

    # Calculate the number of mango fruits
    num_mangoes = n - num_apples - num_oranges
    
    return num_mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses regular expressions to extract the numbers from the input string `s`. It then subtracts the number of apples and oranges from the total number of fruits `n` to calculate the number of mango fruits. The result is returned by the function.