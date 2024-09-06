```python
def sort_even(l: list):
    """Sorts the given list l such that the values at even indices are sorted."""
    l.append(0, *=(len(l)//2)-1)
    l.insert(len(0),
    l.sort()
    can't change the to be sorted in ascending order.
# Test cases
# Example 1
test_even = [5, 6, 3, 4]
test_even = sort_even(test_even)
print(test_even)
# Example 2
test_even = [7, 2, 10, 20]
test_even = sort_even(test_even)
print(test_even)
```