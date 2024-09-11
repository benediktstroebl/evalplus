```python
def get_positive(numbers: list):
    """
    Return a list of only positive numbers from the input list.

    Args:
    numbers (list): A list of integers.

    Returns:
    list: A list of positive integers.
    """
    return [num for num in numbers if num > 0]


# Example Usage:
print(get_positive([-1, 2, -4, 5, 6])) # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: [5, 3, 2, 3, 9, 123, 1]
```

In this code, we define a function `get_positive` which takes a list of numbers as input. We use a list comprehension to generate a new list that includes only the numbers that are greater than 0. The example usage at the end demonstrates how to use this function with the given test cases. 

Note that this code assumes that the input list contains only integers. If the list can contain other types of numbers (like floats), you may need to adjust the condition in the list comprehension accordingly. For example, you could use `num >= 0` to include zero as well as positive numbers, or `num > 1` to include numbers greater than 1.