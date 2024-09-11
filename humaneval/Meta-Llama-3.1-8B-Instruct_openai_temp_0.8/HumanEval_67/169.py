```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number of fruits 
    and the number of apples and oranges in the basket.

    Parameters:
    s (str): A string that represents the total number of the oranges and apples in the basket.
    n (int): An integer that represents the total number of the fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers of apples and oranges from the string
    numbers = list(map(int, re.findall(r'\d+', s)))
    
    # Check if the string contains both "apples" and "oranges"
    if "apples" not in s or "oranges" not in s:
        raise ValueError("The string must contain both 'apples' and 'oranges'.")

    # Calculate the number of mango fruits
    mango = n - sum(numbers)
    
    return mango

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges",3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges",120))  # Output: 19
```