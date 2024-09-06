```python
def sort_even(lst):
    even_list = [x for x in lst if x % 2 == 0]
    return even_list

# Test case 1
assert sort_even([1, 2, 3]) == [1, 2, 3]

# Test case 2
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

# Test case 3
assert sort_even([10, 15, 20]) == [10, 15, 20]
```  This script defines a function `sort_even` that sorts even numbers in a list first, then leaves the rest of the original order.