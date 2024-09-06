```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = [transf_map[int(num) - 1] for num in sorted_arr if num >= 1 and num <= 9]
    return result if result else []
```

The following tests will confirm that the function behaves as expected:
```python
test_1 = ([2, 1, 1, 4, 5, 8, 2, 3], ['One', 'One', 'Two', 'Two', 'Three', 'Four', 'Five', 'Eight'])
test_2 = ([], [])
test_3 = (=[-1, 1, 55], ['One'])
test_4 = (['a', 'b', 'c'], [])
test_list = [test_1, test_2, test_3, test_4]
for t in test_list:
    assert by_length(t[0]) == t[1]
```