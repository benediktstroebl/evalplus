```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    named_arr = [name_digit_map[int(x)] for x in sorted_arr if 1 <= int(x) <= 9]
    return named_arr

def name_digit_map():
    return {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9}
```

The function `by_length` sorts the array, flips it, and then assigns digit names, while ignoring any numbers above 9 or not between 1 and 9. The `name_digit_map` assigns digit numbers to their names and is a dictionary accessible in the module. Would you like to test this function using mock arrays?