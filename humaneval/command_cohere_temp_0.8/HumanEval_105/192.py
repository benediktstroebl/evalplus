Here's a Python script that implements the `by_length` function in a way that fulfills the test cases:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    return [name for num in reversed_sorted_arr for name in {'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'}[num]] if reversed_sorted_arr else []
```

This script sorts the list first by length, then reverses the order, and assigns the corresponding names to the digits. The conditional check for non-emptyness is implicit in this case due to the lack of any return statement in the case of an empty array. The function should work for all arrays that meet the specifications provided. 

The script could be made more efficient by using the built-in `sorted` function's ability to accept a custom `key` function to sort the list once rather than sort it twice.