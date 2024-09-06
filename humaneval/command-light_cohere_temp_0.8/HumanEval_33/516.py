```python
def sort_third(l: list):
    """Sorts a list of integers so that values divisible by three are in their correct positions,
    while other values are in their original positions."""
    c = [i for i in l if i % 3]
    return [i if i not in c else l.find(i) for i in l] + c

#Test case 1
assert sort_third([1, 2, 3]) == [1, 2, 3]

#Test case 2
assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

#Test case 3
assert sort_third([10, 11, 12]) == [11, 12, 10]
```