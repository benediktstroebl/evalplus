```python
def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Args:
        s (str): A string that represents a number of apples and oranges.
        n (int): An integer that represent the total number of the fruits in the basket.

    Returns:
        int: The number of the mango fruits in the basket.
    """
    
    # Split the input string into a list of strings, split by'and '
    s_list = s.split(' and ')
    
    # Create a dictionary to store the count of apples and oranges
    fruit_count = {'apples': 0, 'oranges': 0}
    
    # Iterate over the list of strings and extract the count of apples and oranges
    for fruit_str in s_list:
        if 'apples' in fruit_str:
            fruit_count['apples'] = int(fruit_str.split(' ')[0])
        elif 'oranges' in fruit_str:
            fruit_count['oranges'] = int(fruit_str.split(' ')[0])
    
    # Calculate the count of mangoes by subtracting the count of apples and oranges from the total count
    mango_count = n - fruit_count['apples'] - fruit_count['oranges']
    
    return mango_count

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```