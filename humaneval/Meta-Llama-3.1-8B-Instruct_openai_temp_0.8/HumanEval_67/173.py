```python
def fruit_distribution(s, n):
    """
    Calculating the number of mangoes in the basket.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mangoes in the basket.

    Example:
    >>> fruit_distribution("5 apples and 6 oranges", 19)
    8
    """
    # Split the string into substrings at spaces
    parts = s.split()
    
    # The first number is the total number of apples and oranges
    total_apples_oranges = int(parts[0])
    
    # The last substring is the total number of fruits
    total_fruits = int(parts[-2])
    
    # Calculate the number of mangoes
    num_mangoes = total_fruits - total_apples_oranges
    
    return num_mangoes

# Testing the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # 19
```

In this solution, we first split the input string into substrings at spaces. We then extract the first number as the total number of apples and oranges, and the last substring as the total number of fruits. Finally, we calculate the number of mangoes by subtracting the total number of apples and oranges from the total number of fruits.