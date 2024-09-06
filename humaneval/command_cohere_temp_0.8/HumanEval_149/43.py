```python
def sorted_list_sum(lst):
    lst = [item for item in lst if len(item) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
The Python script solves the problem by filtering out strings with odd lengths from the list and sorting the resulting list in the following way:
1. First, it sorts the list in ascending order based on the length of each string, considering the length as a negative value.
2. If two or more strings have the same length, it sorts them alphabetically in ascending order.

This ensures that the list is sorted in the desired order, with strings of the same length sorted alphabetically and the list itself being filtered of odd-length strings.