Here's a Python script that implements the `by_length` function and demonstrates how to test it using sample cases:
```python
def by_length(arr):
    DIGS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    sorted_arr = sorted(arr)
    reversed_sorted_arr = sorted(sorted_arr)[::-1]
    result = []
    for num in reversed_sorted_arr:
        if 1 <= num <= 9:
            result.append(DIGS[num - 1])
    return result

# Test cases
cases = [
    ([2, 1, 1, 4, 5, 8, 2, 3], ['One', 'One', 'Two', 'Two', 'Three', 'Four', 'Five', 'Eight']),
    ([], ['']),
    ([1, -1, 55], ['One']),
    ([9, 10, 5, 3], ['Nine', 'Ten', 'Five', 'Three'])
]

for arr, expected in cases:
    result = by_length(arr)
    assert result == expected, f"Expected {expected}, but got {result}"
```

In this script, the `by_length` function sorts the input array, reverses the sorted array, and then replaces each digit (`1 <= num <= 9`) with its corresponding name from the DIGS list. The test cases are defined, and the function is tested against each case to verify the expected results.