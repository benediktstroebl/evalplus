```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
        5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
    }
    result = [transf_map[int(dig)] for dig in sorted_arr if dig in transf_map]
    return result if result else []
```

The following tests will check if the function behaves as expected:
```python
def test_by_length():
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    assert by_length([]) == []
    assert by_length([1, -1, 55]) == ['One']
    assert by_length([10, 11, 12]) == []
```

The above test suite contains three assertions that cover every possible case in the `def by_length(arr)` function. Each test is represented by a lowercase letter 'a' to 'c' to follow the alphabetical order of the assertion. You can never have duplicate test names in the same test suite. Adjust the test cases if needed.