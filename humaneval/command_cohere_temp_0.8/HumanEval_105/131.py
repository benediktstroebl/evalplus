Here's a Python script that implements the `by_length` function:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x <= 9 else x)
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    reversed_sorted_names = [
        "One" if x == 1 else
        "Two" if x == 2 else
        "Three" if x == 3 else
        "Four" if x == 4 else
        "Five" if x == 5 else
        "Six" if x == 6 else
        "Seven" if x == 7 else
        "Eight" if x == 8 else
        "Nine" if x == 9 else
        str(x)
        for x in reversed_sorted_arr
    ]
    return reversed_sorted_names
```

This script utilizes Python's `sorted` function with custom key functions to sort the array based on the criteria given. It then reverses the sorted array and assigns corresponding names to each digit, ensuring that the result is correctly formatted.