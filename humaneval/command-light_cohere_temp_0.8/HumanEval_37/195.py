```python
def sort_even(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    return l[:-mod(len(lst),2)] + l[-mod(len(lst),2):]

# Test the function
test_even = [5, 6, 3, 4]
test_even_sorted = sort_even(test_even)
print(test_even_sorted)  # [3, 6, 5, 4]
```