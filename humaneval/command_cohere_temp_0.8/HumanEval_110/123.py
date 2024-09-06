```python
def exchange(lst1, lst2):
    even_exchange = False
    for i in range(len(lst1)):
        if lst1[i] % 2 == 0:
            even_exchange |= lst2[i] % 2
        else:
            even_exchange &= lst2[i] % 2 == 0
    if even_exchange:
        return "YES"
    else:
        return "NO"
```

The function examines each element of both lists using bitwise operations (`|` and `&`) to efficiently check whether it's possible to exchange elements in `lst2` to make `lst1` contain only even numbers. This solution optimally solves the problem in a single pass without extra memory usage, guaranteeing a time complexity of O(n) where `n` is the length of the lists.