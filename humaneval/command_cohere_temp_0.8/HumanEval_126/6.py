```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, count in dups.items():
        if count > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple algorithm that checks if there are any duplicates in the list and if there are, checks if there are more than one of each element, if so the list is not sorted. If there isn't more than one of each element, it checks if the list is sequentially ordered. 

This algorithm can handle the examples provided in a timely manner. And returns the correct values.