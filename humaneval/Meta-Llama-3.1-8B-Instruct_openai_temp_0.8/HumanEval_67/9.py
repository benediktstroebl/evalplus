```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Args:
    s (str): A string that represents a number of apples and oranges 
             distributed in a basket of fruit.
    n (int): An integer that represents the total number of the fruits 
             in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers of apples and oranges
    match = re.search(r"(\d+)\s*apples?\s*and\s*(\d+)\s*oranges?", s)
    
    if match:
        # Extract the numbers of apples and oranges
        apples, oranges = map(int, match.groups())
        
        # Calculate and return the number of mango fruits
        return n - apples - oranges
    else:
        # If the input string does not match the pattern, return -1
        return -1

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # -> 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # -> 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # -> 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # -> 19
```

In this script, I used the `re` module to extract the numbers of apples and oranges from the input string using a regular expression. The regular expression `r"(\d+)\s*apples?\s*and\s*(\d+)\s*oranges?"` matches one or more digits (`\d+`) followed by an optional word "apples" (matched by `apples?`), then "and", and finally another optional word "oranges" (matched by `oranges?`). The `groups()` method returns a tuple of strings where each string corresponds to each group in the match, and the `map()` function converts these strings to integers.