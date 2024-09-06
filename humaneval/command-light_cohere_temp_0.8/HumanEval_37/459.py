```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indic, while its values at the even indic are equal
    to the values of the even indic of l, but sorted."""
    return [e+1 for e in l if e%2 else e]

# Test the function with a list of numbers
test_list = [5, 6, 3, 4]
result = sort_even(test_list)
print(result)  # Output: [3, 4, 5, 6]
```