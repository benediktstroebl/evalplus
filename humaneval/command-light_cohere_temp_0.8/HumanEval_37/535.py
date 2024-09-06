```python
def sort_even(lst):
    return lst[:]  # return empty list for empty input
if not lst:  # empty list
    return []

# split even and odd indexes
even, odd = divmod(len(lst), 2)
even_lst = lst[:even]
odd_lst = lst[even:]

# sort even numbers and equal values to odd
even_lst = sorted(even_lst)
odd_lst = sorted(odd_lst)

# combine sorted even and odd lists
result = even_lst + odd_lst

return result  # return final sorted list
```