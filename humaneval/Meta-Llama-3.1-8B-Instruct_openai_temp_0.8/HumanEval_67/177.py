```python
import re

def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Args:
        s (str): A string that represents the total number of apples and oranges.
        n (int): An integer that represents the total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    numbers = re.findall(r'\d+', s)
    
    # Convert the extracted numbers to integers
    num_apples = int(numbers[0])
    num_oranges = int(numbers[1])
    
    # Calculate the number of mango fruits
    num_mango = n - num_apples - num_oranges
    
    return num_mango

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19)) # Expected output: 8
print(fruit_distribution("0 apples and 1 oranges",3)) # Expected output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Expected output: 95
print(fruit_distribution("100 apples and 1 oranges",120)) # Expected output: 19
```

This script uses regular expressions to extract the numbers of apples and oranges from the input string, then calculates the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits in the basket.