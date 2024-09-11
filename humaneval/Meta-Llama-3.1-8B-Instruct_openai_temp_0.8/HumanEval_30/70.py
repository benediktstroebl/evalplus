```python
def get_positive(l: list):
    """
    Return only positive numbers in the list.
    
    :param l: A list of integers.
    :return: A list of positive integers from the input list.
    """
    return [num for num in l if num > 0]

# Test the function
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]
```

Explanation:

- The `get_positive` function uses list comprehension to create a new list that includes only the numbers from the input list that are greater than 0.
- The function takes a list of integers as input and returns a list of positive integers.
- The test cases at the end of the script demonstrate how to use the function and provide the expected output.