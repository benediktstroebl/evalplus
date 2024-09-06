```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test cases
test_max_element = [
    [
        lst=[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 
        assert max_element(lst) == 123
    ],
    [
        lst=[1, 2, 3, 4, 5, 6],
        assert max_element(lst) == 6
    ],
    [
        lst=[-5, -10, -20, -30, -40, -50, -60, -70, -80, -90],
        assert max_element(lst) == -90
    ],
    [
        lst=[123, 12, 123123, 1234567],
        assert max_element(lst) == 1234567
    ],
    [
        lst=[1, 2, 3, 4, 5],
        Error: Lists have different lengths: ([1, 2, 3], [4, 5])
    ],
    [
        lst=[1, 2, 3, 4, 5],
        Error: Lists have different lengths: ([1, 2, 3], [4, 5, 6])
    ]
]
```
The function `max_element` in this script accepts a list as input and returns the list's maximum element. The test cases make sure that the function will run and validate its accuracy.

The test cases also include a potential error case, where the input lists have different lengths.