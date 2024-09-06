```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal to the values of the even indic of l, but sorted."""
    return [e if e % 2 == 0 else e[::-1] for e in l]

# Test the function
test_list = [5, 6, 3, 4]
test_list2 = [1, 2, 3]

print(sort_even(test_list))  # [3, 6, 5, 4]
print(sort_even(test_list2))  # [1, 2, 3]
``` 
This script defines a function sort_even that takes a list and returns a new list with elements from the original list that are equal to the odd indices of the original list, but sorted. The test_even function is then used to test the function with two different lists, and the output is printed.