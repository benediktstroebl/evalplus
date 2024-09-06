Here's a Python script that implements the `by_length` function with a self-contained code block:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x < 1 or x > 9 else x)
    reverse_arr = sorted(sorted_arr, reverse=True)
    result = []
    for num in reverse_arr:
        if num == 1 or num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 7 or num == 8 or num == 9:
            result.append(
                str(num) if num >= 10 else
                "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".__getitem__(num)
            )
    return result if result != [] else []
```

The provided Python code defines the function `by_length` that takes an array as input and sorts integers from 1 to 9, reverses the array, and converts each digit into its word representation. It ensures that non-digit values are ignored and returns an empty list for empty or invalid input arrays. The code utilizes basic Python sorting and manipulation techniques to achieve the specified problem outcome and handles edge cases appropriately.