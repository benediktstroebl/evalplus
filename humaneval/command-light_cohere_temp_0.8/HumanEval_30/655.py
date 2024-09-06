```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

#Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
assert not get_positive([5, 3, -5, -20])
#This should fail (only -5 will be returned)

#correct usage
print(get_positive([2, 5, 6, 9, 99, -1, 3]))
 ```