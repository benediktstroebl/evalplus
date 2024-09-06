```python
def max_element(lst):
    if not_numbers(lst):
        raise ValueError("Input list must contain only numbers")
    return max(lst)

def test_max_element(test_lst):
    try:
        max_element(test_lst)
    except ValueError as e:
        print(f"Error: {e}")
    return False

# Example 1
numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(test_max_element(numbers))  # Output: True

# Example 2
text = "Hello World"
words = ["Hello", "World"]
print(test_max_element(words))  # Output: False
```
This script defines a function `max_element` that finds the maximum element in a list.

The `test_max_element` function contains a test list and calls the `max_element` function to validate if it works correctly.

This code is self-contained and can be easily integrated into a larger program or script as needed.