```python
def sort_even(lst):
    even = [item for item in lst if item % 2 == 0]
    even.sort(even)
    return even

# Test the function
assert sort_even([1, 2, 3]) == [1, 2, 3]
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
 ```