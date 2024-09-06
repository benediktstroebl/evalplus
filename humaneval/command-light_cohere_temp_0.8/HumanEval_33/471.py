```python
def sort_third(lst):
    """Sorts the list l such that elements not divisible by three are at the beginning"""
    new_lst = []
    for num in lst:
        if num % 3 != 0:
            new_lst.append(num)
    
    return new_lst

# Test cases
test_data = [1, 2, 3, 5, 6, 3, 4, 8, 9, 2]
test_result = sort_third(test_data)
assert test_result == [2, 6, 3, 4, 8, 9, 5]
test_data = [5, 6, 3, 4, 8, 9, 2]
test_result = sort_third(test_data)
assert test_result == [2, 6, 3, 4, 8, 9, 5]
test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_result = sort_third(test_data)
assert test_result == [2, 6, 7, 8, 9, 5, 4, 3, 1]
```