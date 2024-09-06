```python
def pairs_sum_to_zero(l):
    """
    Check if list has two distinct elements whose sum is zero.
    Return True if the causes two numbers that add up to zero in the list, 
    and False otherwise.
    """
    list comprehension is simply: 
    return any(x + y for x, y in l if x + y <= 0)
    """

# Example usage:
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for test in test_cases:
    result = pairs_sum_to_zero(test)
    print(f"{test} => {result}")
```
The function checks whether a list contains two elements whose sum equals zero, returning `True` if this condition is met and `False` otherwise.  The output will either pass corresponding test cases.