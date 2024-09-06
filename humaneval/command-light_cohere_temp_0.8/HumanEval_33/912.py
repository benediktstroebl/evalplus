```python
def sort_third(lst):
    """This function sorts a list l such that numbers not divisible by three are in their original relative order, while numbers divisible by three are sorted equal to each other"""

    # Sort all numbers
    lst = sorted(lst, key=lambda x: x)

    # Remove numbers divisible by three from the list
    lst = [x for x in lst if x not in [3, 6, 9]]

    return lst

# Test the function
assert(sort_third([1, 2, 3]) == [1, 2, 3])
assert(sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5])
```