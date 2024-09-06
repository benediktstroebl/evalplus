```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

#Test cases
test_max_element = [
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], max_element)
    , ( [5, 3, -5, 2, -3], -1)
    , ( [5, 3, -5, 2, -3, 3], None)
    , ( [1, 2, 3, 4, 5, 6], 6)
    , ( [10, 20, 30], None)
]

for item in test_max_element:
    case = item
    x = eval(case[0])  # Create a list from test case
    y = max_element(x)
    assert y == case[1], "Two values do not match!"
```