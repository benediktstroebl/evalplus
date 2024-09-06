```python
def sort_even(lst):
    even_set = set(lst[::index(lst, 2::2)::i])
    lst[:] = [item for item in lst if item not in even_set]
    return lst

# test cases
print(sort_even([1, 2, 3]))     # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```
The function `sort_even` takes a list `lst` as an argument. It creates a particular set of odd elements in the list using the `index()` function and the `::i` slice operator. The list is then filtered with the odd elements removed using a list comprehension. The even elements in the set are then removed from the list. This effectively places the final elements in the list at index 2 and even elements at index 1, while keeping the order of even elements unchanged.