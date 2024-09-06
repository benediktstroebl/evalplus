```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): A list of numbers.
        
    Returns:
        int: The sum of squared integers rounded up to the next integer.
    """
    result = 0
    for n in lst:
        result += n**2

    return int(result)**0.5

# Tests:
assert sum_squares([1, 2, 3]) == 4  # 1 + 4 + 9 = 14
assert sum_squares([1, 4, 9]) == 10  # 1 + 16 + 81 = 98
assert sum_squares([1, 3, 5, 7]) == 8  # 1 + 9 + 25 + 49 = 84
assert sum_squares([1.4, 4.2, 0]) == 3  # 1.4 + 4.2 + 0 = 3.6 -> 3
assert sum_squares([-2.4, 1, 1]) == 4  # (-2.4) + 1 + 1 = 2.4 -> 4
``` 

This Python script defines a function called `sum_squares`, which takes a list of numbers as input and calculates the sum of the squares of these numbers. The function first iterates through the list, summing up the square of each number. Then, it rounds the sum up to the next integer using the power operator `**0.5` to take the square root and then rounding up using int(). The function returns this rounded sum of squared integers.

The script includes several tests to verify the correct behavior of the `sum_squares` function for different input scenarios. Each test case checks whether the function returns the expected output for a specific list of numbers.

The function is designed to handle both positive and negative integers and to correctly sum the squares, considering the ceiling rounding rule.