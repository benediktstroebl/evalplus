```python
def exchange(lst1, lst2):
    even_idx = [i for i, n in enumerate(lst1) if n % 2 == 0]
    if len(even_idx) != len(lst1):
        return "NO"
    lst1[even_idx], lst2[even_idx] = lst2[even_idx], lst1[even_idx]
    return "YES" if all(n % 2 == 0 for n in lst1) else "NO"
```

The approach used in the code is to filter the indices of even numbers from `lst1` and then swap the elements in both lists at these indices. After the swap, we check if all numbers in `lst1` are even and return the respective answer. This algorithm assumes that the input lists are not empty, which is the assumption stated in the problem. Also, the assumption that there is no limit on the number of exchanged elements is reflected in the code, as we swap as many elements as are necessary to make the list of even numbers in `lst1`.