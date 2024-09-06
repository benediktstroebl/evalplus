```python
def sort_third(lst):
    """This function sorts a list l such that values divisible by three are in their correct positions."""
    return sorted(lst, key=lambda x: (x // 3) % 2 == 0)

# Test the function
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_result = sort_third(test_list)
assert test_result == [2, 6, 3, 4, 8, 9, 5, 7, 1, 3] #should be true
```