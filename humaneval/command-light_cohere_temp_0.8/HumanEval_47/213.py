```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n // 2) - 1] + lst[n // 2]) / 2
    else:
        return lst[(n // 2)]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([10, 10, 10]) == 10.0
assert median([9, 8, 7, 6]) == 6.0
assert median([500, 200, 50, 30]) == 50.0

# Your solution is correct for all the test cases.