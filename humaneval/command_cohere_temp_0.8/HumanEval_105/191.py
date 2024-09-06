Here's a Python script that implements the `by_length` function with a self-contained code block:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x < 1 or x > 9 else x)
    reverse_arr = sorted(sorted_arr, reverse=True)
    result = [name for num, name in enumerate(
        ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'], 1)
        if reverse_arr[num] == num]
    return result if result else []
```

This script includes the `by_length` function that takes an array of integers as input and sorts the integers that are between 1 and 9 inclusive, reverse the resulting array, and then replaces each digit by its corresponding name. It returns the list of named digits or an empty list if the input array is empty or contains only strange numbers.