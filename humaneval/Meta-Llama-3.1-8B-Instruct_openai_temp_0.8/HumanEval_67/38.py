```python
import re

def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in the basket.

    Parameters:
    s (str): A string that represents the total number of the oranges and apples.
    n (int): An integer that represent the total number of the fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    numbers = re.findall(r'\d+', s)
    
    # Extract the numbers of apples and oranges
    apples = int(numbers[0])
    oranges = int(numbers[1])
    
    # Calculate the total number of apples and oranges
    total_fruits = apples + oranges
    
    # Return the number of mango fruits
    return n - total_fruits

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19)) # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3)) # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses regular expressions to extract the numbers of apples and oranges from the input string, and then calculates the total number of these fruits. The number of mango fruits is then returned by subtracting this total from the total number of fruits in the basket.