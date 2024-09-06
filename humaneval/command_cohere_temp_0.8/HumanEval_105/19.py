```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', 
                  '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
    result = [transf_map[num] for num in sorted_arr if num <= 9]
    return result if result else []
```

The following tests will confirm that the function behaves as expected:
```python
assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
assert by_length([]) == []
assert by_length([1, -1, 55]) == ['One']
```