```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [ele for ele in sorted_arr if 1 <= ele <= 9]
    reversed_digits = filtered_digits[::-1]
    names = []
    for ele in reversed_digits:
        names.append(ele_to_name(ele))
    return names if names else []

def ele_to_name(ele):
    """Constants for digit names"""
    DIGITS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return DIGITS[ele - 1] if 0 <= ele - 1 < len(DIGITS) else ''

# Testing code
assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
assert by_length([]) == []
assert by_length([1, -1, 55]) == ['One']
``` 

The function by_length sorts the array, retains digits 1 through 9, reverses the digital array, and replaces each digit with its corresponding name. The `ele_to_name` function returns the digit name for a given digit. The DIGITS constant holds the digit names. The function returns an empty list if the input array is empty and only returns the names for included digits if there are any strayed numbers. 

The testing code asserts that the function performs as expected for the example use cases. 

I hope this is helpful! Let me know if you have any questions or need anything else.