```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Args:
        s (str): A string that represents the total number of apples and oranges.
        n (int): The total number of the fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the total number of non-mango fruits
    total_non_mango = apples + oranges
    
    # Return the number of mango fruits by subtracting the total number of non-mango fruits from the total number of fruits
    return n - total_non_mango

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

In this script, we first use regular expressions to extract the number of apples and oranges from the input string. We then calculate the total number of non-mango fruits by adding the number of apples and oranges. Finally, we return the number of mango fruits by subtracting the total number of non-mango fruits from the total number of fruits.