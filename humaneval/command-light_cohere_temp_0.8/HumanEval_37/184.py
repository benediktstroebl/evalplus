```python
def sort_even(lst):
    return lst[:][::2] + lst[:-][1:]

print(sort_even([1, 2, 3]))     # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```