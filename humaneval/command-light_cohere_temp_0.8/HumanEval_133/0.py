```python
def sum_squares(lst):
    """
    Compute the sum of squared numbers in the given list.
    Round each element to the upper integer value.
    Return the simple list comprehension for this
    """
    return sum(map(lambda x: (x ** 2) , lst))

# Example usage:
lst = [1,2,3]
result = sum_squares(lst)
print(result) # Output: 14

# Test with a list with numbers and negative numbers:
lst = [1,4,9,-2]
result = sum_squares(lst)
print(result) # Output: 98

# Test with a list with specific numbers:
lst = [1.4,4.0,4]
result = sum_squares(lst)
print(result) # Output: 29

# Test with a list with specific numbers (Negative), should fail:
lst = [-2.4,1,1]
result = sum_squares(lst)
print(result) # Should raise an error: cannot convert to float
```