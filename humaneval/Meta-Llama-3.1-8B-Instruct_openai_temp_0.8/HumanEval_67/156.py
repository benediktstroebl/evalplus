```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits, 
    apples and oranges.

    Args:
        s (str): A string that represents the total number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers of apples and oranges
    apples_and_oranges = re.findall(r"(\d+)", s)
    
    # Check if the correct number of numbers were extracted
    if len(apples_and_oranges)!= 2:
        raise ValueError("Invalid input string")
    
    # Convert the extracted numbers to integers
    apples = int(apples_and_oranges[0])
    oranges = int(apples_and_oranges[1])
    
    # Calculate the number of mango fruits
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script uses the `re` module to extract the numbers of apples and oranges from the input string using regular expressions. It then calculates the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits. If the input string is invalid (i.e., it does not contain the correct number of numbers), the function raises a `ValueError`.