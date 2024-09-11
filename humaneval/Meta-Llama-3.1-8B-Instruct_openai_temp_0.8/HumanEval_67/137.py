```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number 
    of fruits and a string representing the total number of apples and oranges.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the number of apples and oranges from the string
    apples = int(re.search(r'\d+(?= apples)', s).group())
    oranges = int(re.search(r'\d+(?= oranges)', s).group())
    
    # Calculate the number of mango fruits
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function with the provided examples
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```
This script uses the `re` module to search for the numbers of apples and oranges in the input string. It then subtracts these numbers from the total number of fruits to find the number of mangoes. The function is tested with the provided examples to ensure it works as expected.