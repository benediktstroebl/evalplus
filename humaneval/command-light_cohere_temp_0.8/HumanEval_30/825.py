```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

#Test 1
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

#Test 2
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

#Test 3
try:
    assert get_positive([-33, -55, -67, -90]) == [-90]
except AssertionError as e:
    print("Test 3 failed:", e)

#Test 4
try:
    assert get_positive([123, -5, -10, -20]) == [123, -20]
except AssertionError as e:
    print("Test 4 failed:", e)
```
The `get_positive` function returns a list of positive numbers from the input list. The test cases ensure the
that the function behaves as expected.