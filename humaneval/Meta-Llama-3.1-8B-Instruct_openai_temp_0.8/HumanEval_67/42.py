```python
def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number 
    of fruits and the number of apples and oranges.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the number of apples and oranges
    import re
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    
    return mangoes

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  
print(fruit_distribution("0 apples and 1 oranges", 3))  
print(fruit_distribution("2 apples and 3 oranges", 100))  
print(fruit_distribution("100 apples and 1 oranges", 120))  
```

This script uses the `re.findall()` function to extract the numbers from the string `s`. The `map()` function is then used to convert these numbers into integers. Finally, it calculates the number of mangoes by subtracting the number of apples and oranges from the total number of fruits.