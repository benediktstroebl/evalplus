```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted. """

    note: return type of list is the modified list, not the original"""
    return [x if x % 2 == 0 else x[::-1] for x in l]

# Test cases
test_list = [5, 6, 3, 4]
test_list2 = [1, 2, 3, 4, 5, 6]

print(sort_even(test_list))  # [3, 6, 5, 4]
print(sort_even(test_list2))  # [1, 2, 3, 4, 5, 6]
 ```