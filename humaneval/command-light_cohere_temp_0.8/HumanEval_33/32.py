```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that the list l' is sorted in such a way that values divisible by three appear in ascending order."""
    return [x for x in lst if x % 3 == 0] + [x for x in lst if x % 3 != 0]
# Test cases
test_sort_third = []
test_sort_third.push([1, 2, 3])
test_sort_third.push([5, 6, 3, 4, 8, 9, 2])
test_sort_third.push([5, 6, 3, 4, 8, 9, 5])

# Function call
test_sort_third = sort_third(test_sort_third)

# Print the sorted list
for x in test_sort_third:
    print(x, end=' ')
 ```