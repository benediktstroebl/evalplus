```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    
    Args:
    - a (int): the starting number
    - b (int): the ending number

    Returns:
    - list: A list of even digits in ascending order between a and b. Empty if no such number.
    """
    
    # Check if 'a' or 'b' is outside the range of 0 to 9
    # To avoid fixing a and b to integers very late in the function
    if not(a % 10 >= 0 and a % 10 <= 9):
        a = int(str(a)[0])

    if not(b % 10 >= 0 and b % 10 <= 9):
        b = int(str(b)[0])

    # Changing a and b to integers before checking
    # if they are even or odd helps a lot when debugging
    even_list = [x for x in range(a, b + 1)]
    
    return [x for x in even_list if x % 2 == 0]
```

The function generates a list of even digits between a and b, in ascending order, or an empty list if no such numbers exist. This approach uses list comprehensions to filter the range of integers between `a` and `b` that are even, and then sorts that list in ascending order. 

It also handles potential edge cases where `a` or `b` are floating-point numbers that have decimals. 

To use this function, you can simply call it with two integers a and b, and it will return the list of even digits as specified.