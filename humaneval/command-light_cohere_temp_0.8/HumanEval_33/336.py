```python
def sort_third(l: list):
    """Sorts a list l such that values at indices divisible by three are sorted to the front, and the rest are sorted to the back.
    return: sorted list"""
    l = [x for x in l if x % 3 == 0] + [x for x in l if x % 3 != 0]
    return l

# Test cases
test_sort_third = []
test_sort_third.append([5, [1, 2, 3])
test_sort_third.append([5, [5, 6, 3, 4, 8, 9, 2])
test_sort_third.append([6, [1, 8, 2, 3, 9])

# Function call
result = sort_third(test_sort_third)

# Print the sorted list
print(result)
```