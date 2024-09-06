```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
        5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
        9: 'Nine'
    }
    result = [transf_map[int(i)] for i in sorted_arr if i in transf_map]
    return result if result else []
```

The above code defines a function `by_length` that takes an array of integers as input and sorts integers from 1 to 9, reverses the array, and then transforms each digit to its spoken name. The output is an array of the corresponding names. The code ensures that empty inputs or strange numbers yield appropriate empty outputs.

The following is a test suite that can be used to validate the correctness of the code:
```python
def test_by_length():
    # Test case 1: Basic example
    input_list = [2, 1, 1, 4, 5, 8, 2, 3]
    expected_output = ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    assert by_length(input_list) == expected_output

    # Test case 2: Empty input
    input_list = []
    assert by_length(input_list) == []

    # Test case 3: Ignore strange numbers
    input_list = [1, -1, 55]
    expected_output = ['One']
    assert by_length(input_list) == expected_output

test_by_length()
```

The test suite will evaluate the `by_length` function with various inputs and ensure that it produces the anticipated outcomes.