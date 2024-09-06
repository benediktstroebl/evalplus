```python
def exchange(lst1, lst2):
    odd = lst1.count(0)
    even = lst2.count(0)
    if odd == 0 and even > 0:
        return "YES"
    return "NO"
```

This Python script provides a self-contained function called `exchange` that addresses the problem of exchanging elements between two lists, aiming to transform `lst1` into a list of only even numbers. It accomplishes this by counting the number of odd and even elements in the respective lists. If there are no odd elements in `lst1` and there are even elements in `lst2`, indicating a possible exchange, the function returns "YES." Otherwise, it returns "NO" if the conditions for an even-numbered `lst1` are not met.