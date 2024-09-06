```python
def double_the_difference(nums):
    odd_squares = sum(num**2 for num in nums if num % 2 != 0 and num >= 0 and isinstance(num, int))
    return int(odd_squares)
```

This function `double_the_difference` works for the given problem statement where the sum of squares of odd numbers in the list is calculated. It uses a sum function with a generator expression to calculate the sum of squares for odd numbers in the `nums` list that are not negative integers. The int() function is used to convert the result to an integer, as expected in the problem statement. And the condition `num >= 0 and isinstance(num, int)` is used to ensure that only positive integers are considered. 

The unit tests that can be used to validate the function are:
```python
test_double_the_difference = {
    'Given a list of numbers, return the sum of squares of the numbers in the list that are odd. Ignore numbers that are negative or not integers.:
    () -> 10': {
        'nums': [1, 3, 2, 0],
        'expected': 10,
    },
    'Given a list of numbers, return the sum of squares of the numbers in the list that are odd. Ignore numbers that are negative or not integers.:
    () -> 0': {
        'nums': [-1, -2, 0],
        'expected': 0,
    },
    'Given a list of numbers, return the sum of squares of the numbers in the list that are odd. Ignore numbers that are negative or not integers.:
    () -> 81': {
        'nums': [9, -2],
        'expected': 81,
    },
    'Given a list of numbers, return the sum of squares of the numbers in the list that are odd. Ignore numbers that are negative or not integers.:
    () -> 0': {
        'nums': [0],
        'expected': 0,
    },
    'If the input list is empty, return 0.:
    () -> 0': {
        'nums': [],
        'expected': 0,
    },
}
```