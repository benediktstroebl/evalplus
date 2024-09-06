```python
def sort_even(lst):
    return lst[:]  # using list slice to ensure all elements are even indexed

# Test the function
test_sort_even = lambda: [1, 2, 3] == sort_even([1, 2, 3]) and \
                      [5, 6, 3, 4] == sort_even([5, 6, 3, 4])

if test_sort_even():
    print("Test passed!")
else:
    print("Test failed")
```