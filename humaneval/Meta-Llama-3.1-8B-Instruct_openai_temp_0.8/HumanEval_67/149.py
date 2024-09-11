```python
import re

def fruit_distribution(s, n):
    """
    Calculates the number of mango fruits in a basket given the total number of fruits, 
    and the number of apples and oranges.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the number of apples and oranges from the string
    apples_oranges = re.findall(r'\d+', s)
    
    # Convert the extracted numbers to integers and subtract the total number of apples and oranges from the total number of fruits
    return n - int(apples_oranges[0]) - int(apples_oranges[1])

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses the `re` module to extract the numbers of apples and oranges from the input string using regular expressions. It then converts these numbers to integers and subtracts them from the total number of fruits to find the number of mango fruits.