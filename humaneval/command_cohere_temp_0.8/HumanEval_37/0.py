```python
def sort_even(l: list):
    even = [e for e in l if e % 2 == 0]
    odd = [e for e in l if e % 2 != 0]
    even = sorted(even)
    return odd + even
```

The function "sort_even" takes a list as an argument and returns a list with the odd indices unchanged and the even indices sorted. To do this, it uses two list comprehensions to separate the even and odd indices of the list, sorts the even index values, and then concatenates the two lists with the odd index values at the beginning. You can test this function by calling it with a list and comparing the result to the list with even values sorted at the beginning.