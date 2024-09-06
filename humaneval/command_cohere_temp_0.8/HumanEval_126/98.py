```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in set(dups))
```

This function first checks for duplicates and counts them with each iteration of the list. Then it returns true if there are no duplicates, otherwise, it returns false. The function works under the assumption that the list contains only positive integers and no negative numbers. It also assumes the list elements are integers and not floating point numbers. The function is self-contained as it doesn't import any external libraries but can work with just the Python standard library. It also doesn't rely on any global variables. 
The total time complexity of the is_sorted function is O(n), where n is the number of elements in the input list. The cumulative time complexity of counting duplicates and checking if all duplicates have a count of 1 is O(n). This is a baseline complexity for an algorithm that iterates through the list once.

The space complexity of the function is O(n) as well, due to the necessity of storing the input list in memory, as well as the dictionary for tracking duplicate elements. This is also a baseline complexity since iterating through the list once takes O(n) space.