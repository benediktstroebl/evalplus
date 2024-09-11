```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Args:
    s (str): A string representing the distribution of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    apples, oranges = re.findall(r'\d+', s)
    
    # Convert the extracted numbers to integers
    apples, oranges = int(apples), int(oranges)
    
    # Calculate the total number of apples and oranges
    total_apples_oranges = apples + oranges
    
    # Calculate the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits
    mango_fruits = n - total_apples_oranges
    
    return mango_fruits

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```