Here's a Python script that implements the `by_length` function in a way that fulfills the requirements you've provided:
```python
def by_length(arr):
    validated_arr = [x for x in arr if 1 <= x <= 9]
    sorted_arr = sorted(validated_arr)
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [names[i] for i in reversed_sorted_arr] if reversed_sorted_arr else []
```

This script sorts the validated array, reverses it, and then replaces each digit with its corresponding name starting from 'One'. The function returns an empty list if the input array is empty, and if there are any numbers outside the 1-9 range, they're ignored from the result.