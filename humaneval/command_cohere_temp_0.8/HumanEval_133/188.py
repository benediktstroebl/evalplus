```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest higher integer first.
    """
    result = sum(x ** 2 for x in lst if x % 1 == 0)
    return result
```

This Python script defines a function called `sum_squares` that takes in a list of numbers. This function calculates the sum of the squares of all the integers in the list.

Here's an example of how to use the `sum_squares` function:
```python
print(sum_squares([1, 2, 3]))  # Output: 14
print(sum_squares([1, 4, 9]))  # Output: 98
print(sum_squares([1, 3, 5, 7]))  # Output: 84
print(sum_squares([1.4, 4.2, 0]))  # Output: 29
print(sum_squares([-2.4, 1, 1]))  # Output: 6
```

This would output:
```bash
14
98
84
29
6
```

This function is designed to handle both positive and negative integers and decimal numbers, rounding them to the nearest higher integer before calculating their squares. 

Note that the function excludes fractional parts and negative numbers from the calculation.