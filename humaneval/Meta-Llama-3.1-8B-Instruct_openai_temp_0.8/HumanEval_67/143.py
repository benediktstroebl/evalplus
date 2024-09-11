```python
def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Args:
        s (str): A string that represents the total number of apples and oranges.
        n (int): An integer that represents the total number of the fruits in the basket.

    Returns:
        int: The number of the mango fruits in the basket.
    """
    # Split the string into parts using 'and' as a delimiter
    parts = s.split('and')
    
    # Extract the number of apples and oranges from the string
    num_apples = int(parts[0].split()[-1])
    num_oranges = int(parts[1].split()[0])
    
    # Calculate the number of mangoes by subtracting the number of apples and oranges from the total
    num_mangoes = n - num_apples - num_oranges
    
    return num_mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19)) # 8
print(fruit_distribution("0 apples and 1 oranges", 3)) # 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # 19
```
In this script, the `fruit_distribution` function takes a string `s` and an integer `n` as input. It splits the string into parts using 'and' as a delimiter, extracts the number of apples and oranges from the string, and calculates the number of mangoes by subtracting the number of apples and oranges from the total. The function returns the number of mangoes.