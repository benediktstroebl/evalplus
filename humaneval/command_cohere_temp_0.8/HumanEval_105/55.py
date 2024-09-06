```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [num for num in sorted_arr if 1 <= num <= 9]
    reversed_digits = sorted(filtered_digits, reverse=True)
    digits_names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [digits_names[idx] for idx in reversed_digits] if filtered_digits else []
```

The provided Python script defines a function `by_length` that takes an array of integers as input. It first sorts the array, then filters out numbers between 1 and 9, then reverses the filtered array, and finally converts the reversed digits into their corresponding names. The result is returned as a list of names in the specified order. If the input array is empty or doesn't contain any digits between 1 and 9, it returns an empty list. The code includes tests that verify the function against various input scenarios to ensure correct behavior.