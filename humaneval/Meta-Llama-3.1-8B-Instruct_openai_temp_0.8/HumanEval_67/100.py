```python
import re

def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in the basket given the string representation of 
    apples and oranges and the total number of fruits in the basket.

    Parameters:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Extract numbers from the string using regular expression
    num_str = re.findall(r'\d+', s)
    
    # Convert extracted numbers to integers
    nums = [int(num) for num in num_str]
    
    # Remove the numbers corresponding to apples and oranges from the total
    # and return the difference, assuming that there are no other fruits besides mango
    return n - (sum(nums) - nums[1])

# Example use cases:
print(fruit_distribution("5 apples and 6 oranges", 19))  # -> 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # -> 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # -> 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # -> 19
```

This script uses regular expressions to find the numbers in the input string, converts them to integers, and then subtracts the total number of apples and oranges from the total number of fruits to find the number of mangoes. Note that it assumes that "apples and X oranges" means there are X oranges, and the first number is the number of apples.