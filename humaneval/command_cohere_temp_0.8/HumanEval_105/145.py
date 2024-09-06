```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    result = []
    for num in sorted_arr:
        if 1 <= num <= 9:
            result.append(NUM_TO_NAME[num])
        else:
            result.append(str(num))
    return result

# Dictionary to map digit to its name
NUM_TO_NAME = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}

# Test Cases
arr1 = [2, 1, 1, 4, 5, 8, 2, 3]
expected_result1 = ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']

arr2 = []
expected_result2 = []

arr3 = [1, -1, 55]
expected_result3 = ['One']

test_cases = [([arr1, arr2, arr3], [expected_result1, expected_result2, expected_result3])]

for (test_arr, expected_res) in test_cases:
    result = by_length(test_arr)
    assert result == expected_res, f"Expected {expected_res}, but got {result}"
```

The function by_length sorts the array, reverses it, and then replaces digits with corresponding names. Any number not between 1 and 9 is left as is. Test cases are provided to validate the function.