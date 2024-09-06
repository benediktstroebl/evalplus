```python
def is_sorted(lst):
    dups = {}
    for x in lst:
        if x in dups:
            dups[x] += 1
        else:
            dups[x] = 1
    for x in dups:
        if dups[x] > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
The function uses a simple algorithm that checks if there are any elements in the list that occur more than once, and then checks if the elements are sorted in ascending order. 

The code includes a `dups` dictionary to solve the problem by first checking if there are any duplicate elements and subsequently tracking their occurrences. It iterates through the list, updating the `dups` dictionary with keys being the list elements and values being their occurrences. If a key `x` has a value greater than 1, it means there are duplicates, and the function returns False. If no duplicates are found, the function then checks if the list elements are sorted in ascending order, using a generating expression, and returns True if they are. 

The script would yield the following outputs:
```
True
True
False
True
True
False
True
```