```python
def sort_even(l: list):
    even = [x for x in l if len(x) % 2 == 0]
    odd = [x for x in l if len(x) % 2 != 0]
    return odd + sorted(even)
```

This script provides a function `sort_even` which takes a list as an argument and returns a list with the odd indices unchanged and the even indices sorted. Two lists, `even` and `odd`, are initialized to store the even and odd indexed elements of the input list `l` respectively. These are then concatenated together in the output list, as required by the specification given in the question.