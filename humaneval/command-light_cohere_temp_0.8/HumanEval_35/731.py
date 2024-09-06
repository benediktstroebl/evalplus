```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    else:
        return max(lst)

def not_positive(lst):
    return all(val > 0 for val in lst)

# Example usage
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(test_list))  # Output: 123
print(max_element([0, 0, -5, -20]))  # Output: -20
print(max_element([1, 2, -5, -20]))  # Should raise error
```