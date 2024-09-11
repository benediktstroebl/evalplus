```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Args:
    s (str): A string that represents the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    nums = re.findall(r'\d+', s)
    
    # Check if we were able to extract two numbers
    if len(nums)!= 2:
        raise ValueError("Invalid input string")

    # Convert the extracted numbers to integers
    apples = int(nums[0])
    oranges = int(nums[1].replace(' oranges', '').replace(' oranges', '').replace(' orange', ''))

    # Return the total number of fruits minus the number of apples and oranges
    return n - apples - oranges

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19)) # -> 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # -> 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # -> 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # -> 19
```

This script uses regular expressions to extract the numbers of apples and oranges from the input string, and then returns the total number of fruits minus the number of apples and oranges. It handles cases where the input string is invalid and raises a ValueError.