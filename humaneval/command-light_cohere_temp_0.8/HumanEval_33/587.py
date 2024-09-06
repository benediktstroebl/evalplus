```python
def sort_third(lst):
    # We create a new list filled with the values of the original list, but at a different position
    new_lst = [x for x in lst if x % 3 != 0] + [x for x in lst if x % 3 == 0] + [x for x in lst if x % 3 == 1]
    
    # We sort the newly created list
    return sorted(new_lst)

# We create some tests to check the function
test_sort_third = [
    [
        ('list_with_divisible_3', [1, 2, 3, 4, 6, 8, 9]),
        ('list_without_divisible_3', [5, 6, 3, 4, 8, 9, 2])
    ]
]

# We check if our function is working correctly with our tests
for test in test_sort_third:
    assert sort_third(test[0]) == test[1]
```