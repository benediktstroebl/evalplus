```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number of fruits and the number of apples and oranges.
    
    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.
    
    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the number of apples and oranges from the string
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the total number of apples and oranges
    total_apples_oranges = apples + oranges
    
    # Return the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits
    return n - total_apples_oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # 19
```

In this script, we use the `re` module to extract the number of apples and oranges from the input string. The `findall` function is used with a regular expression to match one or more digits (`\d+`) in the string. The `map` function is then used to convert the extracted numbers from strings to integers. The rest of the function is the same as the problem description.