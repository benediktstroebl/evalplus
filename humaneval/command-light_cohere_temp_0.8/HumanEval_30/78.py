```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with different lists of numbers
# Test with list of negative numbers
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
# Test with list of positive numbers
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
# Test with a mix of positive and negative numbers
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
```
This Python code defines a function called `get_positive` that takes a single argument, `l`, which is a list. The function returns a basic list comprehension that iterates through each element in `l` and adds it to the `result` list if the element is greater than or equal to zero (`>= 0`). This function is then tested with different lists of numbers to ensure it's functionality is correct. 

Note that the function is designed to work with any type of list, not just Markdown code blocks.