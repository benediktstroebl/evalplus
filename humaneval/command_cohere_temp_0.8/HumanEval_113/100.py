```python
def odd_count(lst):
    r = []
    for i, s in enumerate(lst, start=1):
        r.append(f"the number of odd elements in the string {i} of the input.")
        r.append(f"{len([c for c in s if c % 2 == 1])}")
    return r
```

The code uses a simple loop to iterate through the list of strings (lst) and for each string, it calculates the number of odd elements and appends both the textual answer and the numerical representation to the r list. The enumerate function is used to start the enumeration from 1, which aligns with the problem statement's indexing. Finally, the r list is returned as the solution to the problem.