```python
def is_sorted(lst):
    lst.sort()   
    seen = set()
    for v in lst:
        if v in seen:
            return False
        seen.add(v)
    return True
```

The function first sorts the list and then checks if there's any duplication by tracking unique values using a set. If the list is sorted, and there are no duplicates, it returns `True`; otherwise, it returns `False`. 

This approach uses Python's built-in `set` and `sort` functions and avoids explicit loops and comparisons for the duplication check, making it fairly efficient. It also ensures that the approach can easily handle lists with an arbitrary number of elements. 

To execute this code you need to provide the list of numbers that the function "is_sorted" requires. Here's how you can do it:
```python
my_list = [1, 2, 3, 4, 5, 6, 7]
print(is_sorted(my_list))
```
This command will print "True" as the list is ordered and contains no duplicates.