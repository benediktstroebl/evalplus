```python
def sort_even(l: list):
    """Sorts a list of numbers into a list of even numbers and the remaining as odd numbers"""
    l[:::2] = [x for x in l if x % 2 == 0]
    return l

# Test cases
print(sort_even([1, 2, 3]))      # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))    # [3, 6, 5, 4]
print(sort_even([10, 20, 30]))   # [10, 20, 30]
print(sort_even([0, -5, -20])) # [-20, -5, 0]
```