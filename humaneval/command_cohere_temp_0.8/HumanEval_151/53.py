Here's a Python script that contains a function named `double_the_difference` designed to solve the problem statement provided:
```python
def double_the_difference(lst):
    odd_sq = sum(x**2 for x in lst if x % 2 and x >= 0)
    return int(odd_sq)
```

This function employs a list comprehension to determine the sum of squares of odd numbers present in the input list, subsequently converting this sum to an integer using int() in order to ensure a proper return value.

To test this function, you can use the following code:
```python
test_lists = [
    [1, 3, 2, 0],
    [-1, -2, 0],
    [9, -2],
    [0],
    [],
    [10, 5, 8, 4],
]

expected_results = [
    10,
    0,
    81,
    0,
    0,
    0,
]

for test_list, expected in zip(test_lists, expected_results):
    result = double_the_difference(test_list)
    assert result == expected, f"For list {test_list}, expected {expected}, but got {result}"
```

This collection of tests covers a variety of scenarios, confirming that the function appropriately processes both empty lists and lists containing different numbers, whether positive or negative, and whether odd or even.