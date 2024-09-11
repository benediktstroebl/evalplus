```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r'(\d+) apples and (\d+) oranges', s)
    
    # If the pattern is found, extract the numbers and calculate the number of mango fruits
    if match:
        apples, oranges = map(int, match.groups())
        mangoes = n - apples - oranges
    else:
        # If the pattern is not found, return 0
        mangoes = 0
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # -> 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # -> 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # -> 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # -> 19
```

In this script, we use regular expressions to extract the numbers of apples and oranges from the input string. We then subtract these numbers from the total number of fruits to get the number of mango fruits. If the input string does not match the expected pattern, we return 0.