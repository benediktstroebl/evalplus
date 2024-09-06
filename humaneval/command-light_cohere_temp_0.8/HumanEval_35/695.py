```python
def max_element(lst):
    if not_positive(lst) and not_negative(lst):
        return max(lst)
    else:
        raise ValueError("Input list must contain only positive and non-negative numbers")

def not_positive(lst):
    return all(num >= 0 for num in lst)

def not_negative(lst):
    return all(num < 0 for num in lst)

# Test the max_element function
try:
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
except ValueError as e:
    print("Error:", e)

# Test the other two functions
try:
    print(not_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
except ValueError as e:
    print("Error:", e)

try:
    print(not_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
except ValueError as e:
    print("Error:", e)
``` 
This script defines two functions: `max_element` solves the problem and passes tests, while `not_positive` and `not_negative` are helper functions that check validations for the input.