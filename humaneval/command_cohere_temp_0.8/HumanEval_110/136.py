```python
def exchange(lst1, lst2):
    even_idx = [i for i, n in enumerate(lst1) if n % 2 == 0]
    if len(even_idx) != len(lst1):
        return "NO"
    lst1[:], lst2[:] = lst2[even_idx], lst1[even_idx]
    return "YES"
```

The `exchange()` function takes two lists, lst1 and lst2, as input and checks whether it's possible to swap elements between them to make lst1 contain only even numbers. It uses a list comprehension to create an even_idx list, which is a list of indices of even numbers in lst1. The length of this list is checked to see if it's equal to the length of lst1; if it isn't, then there are no even numbers in lst1, and the function returns "NO". Otherwise, a swap is performed between the two lists using simultaneous assignment, and the function returns "YES".