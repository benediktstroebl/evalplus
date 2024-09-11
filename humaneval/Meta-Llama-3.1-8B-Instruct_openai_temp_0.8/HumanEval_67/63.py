```python
import re

def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in a basket given the total number of fruits, 
    oranges, and apples.

    Parameters:
    s (str): A string containing the number of apples and oranges in the format "apples and oranges".
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers from the string
    numbers = re.findall('\d+', s)
    
    # Convert the extracted numbers to integers
    apples, oranges = map(int, numbers)
    
    # Calculate the total number of apples and oranges
    total_fruits = apples + oranges
    
    # Return the number of mango fruits
    return n - total_fruits

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Expected output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Expected output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Expected output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Expected output: 19
```

This script uses regular expressions to extract the numbers from the input string, and then calculates the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits.