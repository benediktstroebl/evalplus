```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_sorted = [num for num in sorted_arr if 1 <= num <= 9]
    return ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][::-1]*len(filtered_sorted)

# Test Cases
arr1 = [2, 1, 1, 4, 5, 8, 2, 3]
expected_result1 = ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']

arr2 = []
expected_result2 = []

arr3 = [1, -1 , 55]
expected_result3 = ['One']

test_cases = [([arr1, arr2, arr3], [expected_result1, expected_result2, expected_result3])]

for (test, expected) in test_cases:
    result = by_length(test)
    assert result == expected
```

The steps involved are:
1. Sort the array based on the digits between 1 and 9.
2. Keep the sorted digits between 1 and 9.
3. Reverse the array of digits.
4. Map each digit to its corresponding name.
5. Return the list of names.