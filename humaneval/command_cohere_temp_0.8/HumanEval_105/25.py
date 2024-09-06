```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
    }
    result = [transf_map[int(num)] for num in sorted_arr if num <= 9 and str(num) in transf_map]
    return result if result else []
```

The following tests will confirm that the function behaves as expected:
```python
test_str = 'Test String'
test_list = [2, 1, 1, 4, 5, 8, 2, 3, 'a', 'b', 'c']
test_empty = []
test_ strang = [1, -1, 55, 'aa', 3.14]

assert by_length(test_list) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
assert by_length(test_str) == []
assert by_length(test_empty) == []
assert by_length(test_strang) == ['One']
```