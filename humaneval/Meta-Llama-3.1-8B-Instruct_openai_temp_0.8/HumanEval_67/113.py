```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket of fruit.

    Args:
    s (str): A string that represents the total number of the oranges and apples.
    n (int): An integer that represent the total number of the fruits in the basket.

    Returns:
    int: The number of the mango fruits in the basket.
    """
    # Use regular expressions to find the numbers of apples and oranges in the string
    numbers = re.findall(r'\d+', s)
    
    # Check if exactly two numbers were found
    if len(numbers)!= 2:
        raise ValueError("Invalid input string")

    # Extract the numbers of apples and oranges
    num_apples = int(numbers[0])
    num_oranges = int(numbers[1])

    # Calculate the number of mango fruits
    num_mango = n - num_apples - num_oranges
    
    return num_mango

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses regular expressions to extract the numbers of apples and oranges from the input string. It then calculates the number of mango fruits by subtracting the numbers of apples and oranges from the total number of fruits in the basket. The result is returned by the function.