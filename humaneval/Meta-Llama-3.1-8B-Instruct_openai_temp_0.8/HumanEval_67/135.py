```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Args:
    s (str): A string that represents the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges
    matches = re.findall(r'\d+', s)
    
    # Extract the numbers of apples and oranges
    nums = [int(match) for match in matches]
    
    # Check if the given string contains both 'apples' and 'oranges'
    if len(nums)!= 2 or 'apples' not in s or 'oranges' not in s:
        raise ValueError("Invalid input. The string should contain both 'apples' and 'oranges'.")

    # Calculate the number of mangoes
    mangoes = n - nums[0] - nums[1]
    
    return mangoes

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses regular expressions to extract the numbers of apples and oranges from the input string. It then calculates the number of mangoes by subtracting the numbers of apples and oranges from the total number of fruits. If the given string does not contain both 'apples' and 'oranges', it raises a ValueError.