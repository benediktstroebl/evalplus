```python
def max_element(lst):
    if not_decimal(lst) and not_negative(lst):
        return max(lst)
    else:
        raise ValueError("Input list must contain only positive integers")

def test_max_element(lst):
    try:
        return max_element(lst)
    except ValueError as e:
        print(f"Error: {e}")

# Example usage
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(test_max_element(input_list))  # Output: 123

input_list_negative = [-5, 3, -10, 2]
print(test_max_element(input_list_negative))  # Output: ValueError: Input list must contain only positive integers

input_list_decimal = [1.2, 3. either 1, but integers, floats, and empty strings)
print(test_max_element(input_list_decimal))  # Output: ValueError: Input list must contain only positive integers
```

This code defines a function max_element that calculates the maximum element in a list of integers, and tests the input to ensure it contains only positive integers. It also has a script test_max_element, which calls the max_element function on a sample list and handles exceptions gracefully. Finally, an example input list is provided and tested, with the results printed.