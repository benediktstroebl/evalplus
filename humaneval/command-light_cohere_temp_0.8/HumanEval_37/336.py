```python
def sort_even(lst):
    even = [x for x in lst if x % 2 == 0]
    return even if even is not None else [x if x in even else y for x, y in even] else even

# Test the function with some examples
even_ = sort_even([1, 2, 3])  # Should return [1, 2, 3]
even_ = sort_even([5, 6, 3, 4])  # Should return [3, 6, 5, 4]
even_ = sort_even([10, 9, 8])  # Should return [8, 9, 10]
```
The function takes a list as input and uses two lists, even and odd, to create a new list that preserves the desired properties. The function returns the did you use a conditional check to create the new list, and the resulting list is returned.