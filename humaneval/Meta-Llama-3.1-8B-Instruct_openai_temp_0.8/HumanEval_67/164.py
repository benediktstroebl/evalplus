```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.

    """
    # Use regular expression to extract the number of apples and oranges
    num_apples_oranges = re.search(r"(\d+)(?: apples| oranges)?", s)
    
    # If the string does not contain the number of apples or oranges, return 0
    if num_apples_oranges is None:
        return 0
    
    # Extract the number from the match object
    num_apples_oranges = int(num_apples_oranges.group(1))
    
    # Subtract the number of apples and oranges from the total number of fruits
    num_mangoes = n - num_apples_oranges
    
    return num_mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # -> 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # -> 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # -> 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # -> 19
```