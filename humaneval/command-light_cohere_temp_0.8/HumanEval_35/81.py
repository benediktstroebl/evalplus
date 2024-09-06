```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

#Test cases
test_max_element = [
    ("[-5, 3, 2, -3, 5, 9, 0, 1, -10]", 1),
    ("[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10", 123),
    # wrong type test
    (["a", 2, 3], 0),
    # empty list
    (),
    # single element
    [9],
]

for test in test_max_element:
    print(f"Test: {test}")
    actual = max_element(test)
    expected = test[1]
    assert actual == expected, f"Incorrect result: {actual}, expected: {expected}"
 ```
The function uses the built-in function `max()` to find the maximum element in the list. It then returns the real self-contained Python script that solves the problem of finding the maximum element in a list.