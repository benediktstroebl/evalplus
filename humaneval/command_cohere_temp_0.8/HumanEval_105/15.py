Here's a Python script that implements the `by_length` function and gets the expected output:
```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [num for num in sorted_arr if 1 <= num <= 9]
    reversed_digits = sorted(filtered_digits, reverse=True)
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [names[i] for i in reversed_digits] if filtered_digits else []
```

The script first sorts the input array, then filters out numbers between 1 and 9, then reverses this filtered array, and then returns the corresponding names for each digit. The function result is an empty list if the input array is empty or only contains numbers outside the specified range.