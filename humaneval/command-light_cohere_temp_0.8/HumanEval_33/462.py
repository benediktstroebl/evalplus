```python
def sort_third(l: list):
    """Sorts a list so that values not divisible by three are at the beginning, and the values divisible by three are at the end"""
    return l[:len(l)//3] + [x for x in l if x%3 == 0] + l[-len(l)//3:]

#Test cases
assert(sort_third([1, 2, 3]) == [1, 2, 3])
assert(sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5])
assert(sort_third([10, 2, 4, 6, 8, 9]) == [2, 4, 6, 8, 9, 10])
```