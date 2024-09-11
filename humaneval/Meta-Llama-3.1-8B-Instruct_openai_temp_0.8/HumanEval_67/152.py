```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the number of apples, oranges, 
    and total fruits.

    Args:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the number of apples and oranges from the string
    num_apples, num_oranges = map(int, re.findall(r'\d+', s))
    
    # Subtract the total number of apples and oranges from the total number of fruits
    num_mangoes = n - num_apples - num_oranges
    
    return num_mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19)) # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

In this script, we use the `re.findall` function to extract the numbers of apples and oranges from the input string. The numbers are then converted to integers and subtracted from the total number of fruits to calculate the number of mangoes. The test cases at the end verify that the function works as expected.