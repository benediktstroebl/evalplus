```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    res = [transf_map[int(num) - 1] for num in sorted_arr if 1 <= int(num) <= 9]
    return res if res else []
```

The following tests will confirm that the function behaves as expected:
```python
test_list = [([2, 1, 1, 4, 5, 8, 2, 3], ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']),
            ([], []),
            ([1, -1, 55], ['One'])]

for arr, ans in test_list:
    assert by_length(arr) == ans
```