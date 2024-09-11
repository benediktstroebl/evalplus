```python
import re

def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Parameters:
    s (str): A string that represents the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    fruits = re.findall(r'\d+', s)
    
    # If the string does not contain the numbers of apples and oranges
    if len(fruits) < 2:
        return n - int(fruits[0]) if fruits else n
    
    # Calculate the total number of apples and oranges
    total_apples_oranges = sum(map(int, fruits))
    
    # Return the number of mango fruits
    return n - total_apples_oranges

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19)) # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```
This script uses regular expressions to extract the numbers of apples and oranges from the string, then calculates the total number of these fruits and subtracts it from the total number of fruits in the basket to get the number of mango fruits. The script includes test cases to verify its correctness.