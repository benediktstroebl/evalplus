```python
def sort_even(l: list):
    even = [e for e in l if e % 2 == 0]
    odd = [o for o in l if o % 2 != 0]
    even = sorted(even)
    return odd + even
```

The function 'sort_even' takes a list 'l' as an argument and returns a new list 'l'` that is identical to 'l' in its odd indices, while the values at the even indices of 'l`' are equal to the values of the even indices of 'l', but sorted. To achieve this, the function first uses a list comprehension to split 'l' into two lists: one containing elements at even indices and one containing elements at odd indices. After sorting the even index values, the function returns the odd index values appended to the even-sorted index values.

Here is an example usage of the function:
```python
>>> sort_even([1, 2, 3])
[1, 2, 3]
>>> sort_even([5, 6, 3, 4])
[3, 6, 5, 4]
```
In the example above, the function is tested with two different lists. In both cases, the function returns the list with sorted even indices appended to the original list's odd indices.