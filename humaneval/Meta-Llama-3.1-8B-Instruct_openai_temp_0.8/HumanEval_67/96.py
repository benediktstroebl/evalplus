### Fruit Distribution Problem Solution
```python
import re

def fruit_distribution(s, n):
    """
    Calculates the number of mango fruits in a basket given the total number of fruits and the number of apples and oranges.

    Parameters:
    s (str): A string containing the number of apples and oranges in the format "X apples and Y oranges".
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the total number of apples and oranges
    total_apples_oranges = apples + oranges
    
    # Return the difference between the total number of fruits and the total number of apples and oranges
    return n - total_apples_oranges

# Example usage:
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```
This Python script uses regular expressions to extract the numbers of apples and oranges from the input string, and then calculates the total number of mango fruits in the basket by subtracting the total number of apples and oranges from the total number of fruits. The result is returned as an integer.