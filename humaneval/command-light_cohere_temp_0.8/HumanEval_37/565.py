```python
def sort_even(l: list):
    return l[:]
#Test case 1
assert sort_even([1, 2, 3]) == [1, 2, 3]
#Test case 2
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
#Test case 3
l = [10, 20, 30, 40]
assert sort_even(l) == [10, 20, 30, 40]
 ```