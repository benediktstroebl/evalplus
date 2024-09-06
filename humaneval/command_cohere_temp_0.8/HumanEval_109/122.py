Here's a Python script that contains a function named `move_one_ball` with the specified problem statement. The function returns `True` if it's possible to sort the array in non-decreasing order by performing right shift operations. Otherwise, it returns `False`. The script also includes a set of tests to verify the function's correctness:
```python
def move_one_ball(arr):
    nums = list(arr)
    nums.sort()
    if arr == nums or not nums:
        return True
    return False

# Tests
tests = [
    [ [3, 4, 5, 1, 2], True ],
    [ [3, 5, 4, 1, 2], False ],
    [ [1, 2, 3, 4, 5], True ],
    [ [5, 4, 3, 2, 1], False ],
    [ [1], True ],
    [ [], True ],
    [ [], False ],
]

for test in tests:
    assert move_one_ball(test[0]) == test[1]
```

You can use these test cases to validate the correctness of your solution. Adjust the test cases if needed to cover edge cases and further refine your solution's behavior.