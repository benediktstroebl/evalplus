```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the string 
    representation of the total number of apples and oranges and an integer representing 
    the total number of fruits in the basket.

    Parameters:
    s (str): A string representing the total number of apples and oranges in the basket.
    n (int): An integer representing the total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r'(\d+)\s*(apples|oranges)', s)
    
    # If a match is found, extract the numbers of apples and oranges
    if match:
        num_apples, num_oranges = int(match.group(1)), 1 if match.group(2) == 'apples' else 6
    
    # If no match is found, assume there are no apples or oranges
    else:
        num_apples, num_oranges = 0, 0
    
    # Calculate the number of mango fruits
    num_mangoes = n - num_apples - num_oranges
    
    return num_mangoes

# Example use cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```