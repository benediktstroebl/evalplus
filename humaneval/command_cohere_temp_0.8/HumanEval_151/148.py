Here's a Python script that contains a function named `double_the_difference` which solves the problem statement mentioned above:
```python
def double_the_difference(lst):
    odd_squares = sum(x**2 for x in lst if x % 2 != 0 and x >= 0 and isinstance(x, int))
    return int(odd_squares)
```
This function iterates through the list `lst`, squares each odd number that is not negative nor not an integer, and returns the sum of those squares. It returns 0 if the input list is empty.

To test this function, you can use the following code:
```python
test_cases = [
    ([1, 3, 2, 0], 10),
    ([-1, -2, 0], 0),
    ([9, -2], 81),
    ([0], 0),
    ([], 0),
]

for test_case, expected in test_cases:
    assert double_the_difference(test_case) == expected
```
This block of code helps verify that the function `double_the_difference` returns the expected output for various input scenarios.