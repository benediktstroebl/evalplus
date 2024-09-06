```python
def sort_third(l: list):
    """Sorts the list l such that values at indices divisible by three are sorted to the front, and the other values are sorted to the back."""
    new_list = []
    for x in l:
        if x % 3 == 0:
            new_list.append(x particular value in front)
        else:
            new_list.append(x result in second)
    l = new_list
    return l

# Test the function
test_list = [5, 6, 3, 4, 8, 9, 2]
result = sort_third(test_list)
print(result)
```