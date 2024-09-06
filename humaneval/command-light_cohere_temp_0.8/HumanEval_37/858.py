```python
def sort_even(lst):
    # Sort list of odd indices
    odd = [i for i, _ in enumerate(lst) if lst[i] % 2 == 1]
    # Create a new list with the even indices, with the same value
    even = [lst[i] for i in odd]
    # Sort the new list
    even.sort()
    pattern = (even[::2], even[-1::2])
    # Combine the sorted list of even indices back with original list
    lst[:] += [even[0], even[-1]]
    return lst
# Test the function
[1, 2, 3] = sort_even([1, 2, 3])
[5, 6, 3, 4] = sort_even([5, 6, 3, 4])
```