```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list `even_odd` that stores the even integers positioned at odd indices from the input list. It traverses the list, checking if the index is odd and the element is even, then adding it to `even_odd`. Finally, the function returns this list. 

The following example illustrates its usage:
```python
>>> add([4, 2, 6, 7])
[2]
```