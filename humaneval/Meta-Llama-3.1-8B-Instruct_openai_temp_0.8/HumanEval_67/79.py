```python
def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in the basket given a string representing the total 
    number of apples and oranges and an integer representing the total number of fruits.
    
    Parameters:
    s (str): A string that represents the total number of the oranges and apples.
    n (int): An integer that represents the total number of the fruits in the basket.
    
    Returns:
    int: The number of the mango fruits in the basket.
    """
    
    # Split the string into parts and extract the numbers using regular expressions
    import re
    num_apples = int(re.search(r"(\d+) apples", s).group(1))
    num_oranges = int(re.search(r"(\d+) oranges", s).group(1))
    
    # Calculate the total number of apples and oranges
    total_apples_oranges = num_apples + num_oranges
    
    # Return the difference between the total number of fruits and the total number of apples and oranges
    return n - total_apples_oranges

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script uses the `re` module to extract the numbers from the string using regular expressions. The `search` function is used to search for the pattern in the string, and the `group` function is used to extract the matched string. The numbers are then converted to integers and subtracted from the total number of fruits to get the number of mango fruits.