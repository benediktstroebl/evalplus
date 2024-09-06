```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [val for val in sorted_arr if 1 <= val <= 9]
    reversed_digits = filtered_digits[::-1]
    named_digits = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [named_digits[idx] for idx in reversed_digits]

# Test Cases
assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
assert by_length([]) == []
assert by_length([1, -1, 55]) == ['One']
``` 

This code first sorts the array of integers from 1 to 9, then filters out the digits from the sorted array, reverses the filtered digits array, and then maps each digit to its corresponding name from "One" to "Nine". Finally, it returns the list of named digits in the reverse order. 

The test cases are asserted to verify the function's correctness. You can add more test cases to increase test coverage and ensure the function handles various scenarios properly.