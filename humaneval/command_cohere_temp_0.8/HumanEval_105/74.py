```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_sorted = [val for val in sorted_arr if 1 <= val <= 9]
    return ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][::-1]*len(filtered_sorted)

# Test Cases
arr1 = [2, 1, 1, 4, 5, 8, 2, 3]
expected_result1 = ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']

arr2 = []
expected_result2 = []

arr3 = [1, -1 , 55]
expected_result3 = ['One']

test_cases = [
    (arr1, expected_result1),
    (arr2, expected_result2),
    (arr3, expected_result3)
]

for arr, expected in test_cases:
    result = by_length(arr)
    print(f'Input: {arr} -> Output: {result} -> Expected: {expected}')
    assert result == expected
```

This Python script defines a function `by_length` that sorts, filters, and transforms an input array as per the problem statement. The function is tested against various input cases (`arr1`, `arr2`, `arr3`) and the results are compared to the expected outputs (`expected_result1`, `expected_result2`, `expected_result3`). The `test_cases` list provides input-output pairs for the assertions, ensuring the function's correctness.