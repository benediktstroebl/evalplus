```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = [transf_map[int(num)] for num in sorted_arr if 1 <= int(num) <= 9]
    return result if result else []
```

The following tests will confirm that the function behaves as expected:
```python
# Correct behavior tests
assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
assert by_length([]) == []

# Edge case tests
assert by_length([1, -1, 55]) == ['One']
assert by_length([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'One']
```