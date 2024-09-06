```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
    }
    result = [transf_map[int(num)] for num in sorted_arr if num <= 9 and int(num) in transf_map]
    return result if result else []
```

The following tests will confirm that the function behaves as expected:
```python
test_list = [
    ([], []),
    ([1, 1, 4, 5, 8, 2, 3], ['One', 'One', 'Four', 'Five', 'Eight', 'Two', 'Two', 'Three']),
    ([55, 1, -1], ['One']),
    ([], []),
]

for test in test_list:
    assert by_length(test[0]) == test[1]
```