```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the string 
    representing the total number of oranges and apples and the total number of fruits 
    in the basket.

    Parameters:
    s (str): A string representing the total number of oranges and apples.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to find the total number of apples and oranges
    apples, oranges = map(int, re.findall(r"(\d+) apples and (\d+) oranges", s)[0])
    
    # Calculate the total number of fruits
    total_fruits = apples + oranges
    
    # Return the number of mango fruits
    return n - total_fruits

# Example usage:
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

In this code, we use the `re` module to find the total number of apples and oranges in the string `s` using a regular expression. We then calculate the total number of fruits by adding the number of apples and oranges. Finally, we return the difference between the total number of fruits `n` and the total number of apples and oranges.