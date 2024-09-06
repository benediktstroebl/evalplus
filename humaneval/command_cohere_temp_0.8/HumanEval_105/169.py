```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_sorted = [val for val in sorted_arr if 1 <= val <= 9]
    return [name_digit_map[int(val)] for val in filtered_sorted[::-1]]

def digit_name_map():
    return ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

name_digit_map = digit_name_map()
```

The function by_length takes an input array and sorts, filters, and maps digits to names, all within a single function. The digit_name_map function is a helper function to create the name_digit_map dictionary. Together, these functions fulfill the problem requirements.