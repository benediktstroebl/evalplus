```python
def sorted_list_sum(lst):
    lst = [e for e in lst if len(e) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This function takes a list lst as input, which contains strings with odd-length elements removed, and returns a sorted list while still maintaining the integrity of the provided example scenarios. It removes any element with an odd length using a list comprehension and sorts the list using the sort method with a custom sorting key. The key is a lambda function that prioritizes sorting by the length of each string in descending order and then alphabetically if the length is the same.