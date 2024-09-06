```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.

    Parameters:
    l (list): a list of numbers
    Returns:
    l' (list): a sorted list with even indexes having the same value."""
    l[:odd] = l[:odd] + [l[even]]
    return l'

# test the function
test_even = sort_even([1, 2, 3])
test_even = [x for x in test_even if x != test_even[0]]
test_even = [x for x in test_even if x != test_even[-1]]
test_even = sorted(test_even)
print(test_even)
 ```