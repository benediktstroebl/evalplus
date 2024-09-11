Here's a self-contained Python script that solves the problem using regular expressions:

```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Parameters:
    s (str): A string representing the number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers of apples and oranges
    matches = re.findall(r'\d+', s)
    
    # Convert the extracted numbers to integers
    apples = int(matches[0])
    oranges = int(matches[1])
    
    # Calculate the number of mango fruits
    mangoes = n - apples - oranges
    
    return mangoes

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # 19
```

In this script, we use the `re.findall()` function to extract the numbers of apples and oranges from the string `s`. We then convert these numbers to integers and subtract them from the total number of fruits `n` to get the number of mango fruits. The result is returned by the function. The script also includes test cases to demonstrate its usage.