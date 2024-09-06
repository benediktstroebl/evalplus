```python
def choose_num(x, y):
    max_even = max(x, y) if (x == y) or (x % 2 == y % 2) else -1
    return max_even if max_even >= x and max_even <= y else -1

# Test Cases
assert choose_num(12, 15) == 14
assert choose_num(13, 12) == -1
assert choose_num(2, 4) == 4
assert choose_num(100, 200) == 198
```

This function takes in two parameters, x and y, representing the upper and lower bounds of a non-empty range of positive integers. The function seeks the largest even integer within this range, toggling between the maximum of the two numbers and -1 as appropriate. This is achieved through the expression `max_even = max(x, y) if (x == y) or (x % 2 == y % 2) else -1`.

The function will return -1 in two situations:
1. When the range is empty, defined as `max_even < x or max_even > y`.
2. When no even integer exists within the range. This second condition is checked with the clause `max_even if max_even >= x and max_even <= y`. If the condition is false, the function returns -1.

The script also includes test cases to help ensure that the function is working correctly. You can add more test cases as needed.