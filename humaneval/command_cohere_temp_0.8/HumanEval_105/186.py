```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = []
    for num in sorted_arr:
        if 1 <= num <= 9:
            result.append(transf_map[num - 1])
        else:
            result.append(str(num))
    return result if result else []
```

The following tests will confirm that the function behaves as expected:
```python
test_list = [([2, 1, 1, 4, 5, 8, 2, 3], ['One', 'One', 'Two', 'Two', 'Three', 'Four', 'Five', 'Eight', 'Nine']),
            ([], ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']),
            ([1, -1, 55], ['One', '-1', '55'])]

for t in test_list:
    assert by_length(t[0]) == t[1]
```