```python
def sort_even(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd indic,
    while its values at the even indices are equal to the values of the even indicies of l, but sorted."""
    new_even = [x for x in l if x % 2 == 0]
    new_odd = [x for x in l if x % 2 != 0]
    return new_even + new_odd
# Example usage:
if __name__ == "__main__":
    test_list = [5, 6, 3, 4]
    sort_even(test_list)
    expected = [3, 6, 5, 4]
    print("Test passed:")
    print(test_list == expected)
```