Here's a Python script that implements the `by_length` function with a self-contained code block:
```python
def by_length(arr):
    DIGS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    if not arr:
        return []
    sorted_arr = sorted(arr)
    reversed_sorted_arr = sorted_arr[::-1]
    result = []
    for num in reversed_sorted_arr:
        if 1 <= num <= 9:
            result.append(DIGS[num - 1])
    return result
```

This script provides a function `by_length` that takes an array of integers as input and sorts the integers between 1 and 9 inclusive, reverse the sorted array, and then replace each digit by its corresponding name from "One" to "Nine". The function handles cases where the array is empty or contains strange numbers.