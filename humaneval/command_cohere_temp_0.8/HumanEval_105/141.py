Here's a Python script that implements the `by_length` function and demonstrates how to test it using example inputs and expected outputs:
```python
def by_length(arr):
    DIGITS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    sorted_arr = sorted(filtered_arr)
    reversed_arr = sorted_arr[::-1]
    result = [DIGITS[i] for i in reversed_arr]
    return result if result else []

# Test cases
assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
assert by_length([]) == []
assert by_length([1, -1, 55]) == ['One']
```

This code snippet defines the `by_length` function to sort, reverse, and rename digits in the input array according to the problem statement. It also includes test cases to validate the function's behavior against expected outputs. Adjust the test cases as needed based on different scenarios you want to cover.