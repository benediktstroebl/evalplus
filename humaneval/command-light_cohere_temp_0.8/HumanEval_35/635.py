```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    else:
        return max(lst)

def not_positive(lst):
    return all(x > 0 for x in lst)

# Test the function with various list inputs
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: 123
print(max_element([-1, 2, 3, 4, -5]))          # Output: 3
print(max_element([18, 9, 2, 8, 10, 0]))       # Output: 10
print(max_element([1, 2, 3, 4, 5, 6, 7, 8]))   # Output: 5
```