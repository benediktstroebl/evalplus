Here's a Python script with a self-contained function that solves the problem and includes helpful messages when the function is called with a test case:
```python
def double_the_difference(lst):
    """
    Sum of squares of odd integers from the list, while ignoring negative or non-integer numbers.

    :param lst: List of numbers.
    :return: Sum of squares of odd integers or 0 if the list is empty.
    """
    result = 0
    for num in lst:
        if num % 2 == 1 and num >= 0 and isinstance(num, int):
            result += num ** 2

    return result

# Test cases
print(f"Test case 1: {double_the_difference([1, 3, 2, 0]) == 10}")
print(f"Test case 2: {double_the_difference([-1, -2, 0]) == 0}")
print(f"Test case 3: {double_the_difference([9, -2]) == 81}")
print(f"Test case 4: {double_the_difference([0]) == 0}")
print(f"Test case 5: {double_the_difference([1, -1, 1, 1]) == 2}")
```

To execute the code, run it in your Python environment. The script includes five test cases, and it should print out messages indicating whether each test case resulted in a successful validation or not.