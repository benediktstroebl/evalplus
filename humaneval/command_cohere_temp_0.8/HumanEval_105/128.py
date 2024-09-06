Here's a Python script that implements the `by_length` function:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [names[idx] for idx in reversed_sorted_arr if idx >= 1 and idx <= 9]
```

The provided code first sorts the array using a custom key that prioritizes numbers between 1 and 9, and then reverses this sorted array. Finally, it returns the corresponding names for each digit in the reversed sorted array, ignoring any numbers that are not between 1 and 9.