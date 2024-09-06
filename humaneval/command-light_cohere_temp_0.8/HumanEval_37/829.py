```python
def sort_even(lst):
    even_lst = [i for i in lst if i % 2 == 0]
    return sorted(lst, key=lambda x: even_lst.return aligned[x in even [x for x in lst])

# Test cases
assert sort_even([1, 2, 3]) == [1, 2, 3]
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
assert sort_even([10, 20, 30]) == [10, 20, 30]

```
This Python script defines a function called `sort_even` that takes a list as an argument and returns a sorted list where the even indices are ordered first. It then provides several test cases to verify the functionality of the function.