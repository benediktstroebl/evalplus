Here's a Python script that implements the `by_length` function with a self-contained code block:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    named_reversed_sorted_arr = ['Zero'] * (len(reversed_sorted_arr) - 1) + ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [named_reversed_sorted_arr[idx] for idx in reversed_sorted_arr if idx <= 9]

# Test Cases
assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
assert by_length([]) == []
assert by_length([1, -1, 55]) == ['One']
```

This script includes the `by_length` function that sorts the input array based on the length of digits, then reverses the sorted array, and finally assigns corresponding names to the digits. It also comes with test cases to validate its functionality. You can easily adapt this code block to your problem statement and add more tests to thoroughly evaluate the solution. 

Let me know if you need anything else!