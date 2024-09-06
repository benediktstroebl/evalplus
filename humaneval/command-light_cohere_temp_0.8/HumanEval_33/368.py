```python
def sort_third(lst):
    # list comprehension: creates a new list of integers from lst, except the multiples of three
    return [x for x in lst if x % 3 != 0]

# tests
print(sort_third([1, 2, 3]))  # expected output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # expected output: [2, 6, 3, 4, 8, 9, 5]
```