```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t`. If all comparisons are below the threshold, it returns `True`, or else `False`. 

Here is a test case to ensure the function runs correctly:
```python
test_cases = [
    ([1, 2, 4, 10], 100, True),
    ([1, 20, 4, 10], 5, False),
    ([-5, -10, -15, -20], -15, False)
]
```

You can then use the test_cases list to feed multiple inputs to the function and verify its correctness:
```python
for test in test_cases:
    input_list, threshold, expected = test
    actual = below_threshold(input_list, threshold)
    assert actual == expected
```

This provides an accurate test of the function using different inputs to ensure its correctness in determining whether a list of numbers is all below a given threshold.