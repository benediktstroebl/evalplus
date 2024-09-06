Here's a Python script that implements the `by_length` function in a way that is both self-contained and efficient:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: [x] == ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].index(x))
    return ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][::-1]*len(sorted_arr)
```
This approach first sorts the array of integers based on digit names, then reverses the sorted array, and constructs the resulting array of digit names of the appropriate length.