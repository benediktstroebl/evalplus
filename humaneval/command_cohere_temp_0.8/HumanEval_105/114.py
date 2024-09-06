```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
    }
    result = [transf_map[int(dig)] for dig in sorted_arr if 1 <= int(dig) <= 9]
    return result if result else []
```

The above function utilizes a dictionary named `transf_map` to translate digits to their corresponding names. The digits are then sorted in descending order, reversed to retain the original order, and then translated. Lastly, the function returns the resultant list or an empty list if the original array was empty. 

Here is a test suite to ensure the function behaves as intended:
```python
def test_by_length():
    # No strange numbers, all digits translated
    arr = [1, 1, 2, 2, 3, 4, 5, 8, 9]
    expected = ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One', 'One']
    assert by_length(arr) == expected

    # No strange numbers, some digits skipped
    arr = [7, 4, 1, 1, 4, 5, 8, 2, 3]
    expected = ['Seven', 'Four', 'One', 'One', 'Four', 'Five', 'Eight', 'Two', 'Two', 'Three', 'Three']
    assert by_length(arr) == expected

    # Strange numbers ignored
    arr = [1, -1, 55, 4, 5, 8, 2, 3]
    expected = ['One']
    assert by_length(arr) == expected

    # Empty list
    arr = []
    assert by_length(arr) == []

test_by_length()
``` 

The test suite contains multiple test functions to comprehensively test the `by_length` function with different scenarios. 
The first test verifies that all digits are translated and there are no strange numbers, whereas the second test verifies the function's behavior when some digits are skipped and there are strange numbers present. The third test verifies that the function can handle an empty list and returns an empty list as well.  The final function `test_by_length()` executes the test suite.