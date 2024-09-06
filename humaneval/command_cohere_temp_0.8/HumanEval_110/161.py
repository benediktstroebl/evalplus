```python
def exchange(lst1, lst2):
    even_exchange = False
    for x in lst1:
        if type(x) == int and x % 2 == 0:
            even_exchange = True
            break
    if even_exchange:
        for x in lst2:
            if type(x) == int and x % 2 != 0:
                even_exchange = False
                break
    if even_exchange:
        return "YES"
    else:
        return "NO"
```

The `exchange()` function takes two lists, `lst1` and `lst2`, as input. It first checks `lst1` to see if it contains any even numbers. If an even number is found, it sets a flag `even_exchange` to `True`. If no even numbers are found in `lst1`, it will check `lst2` for the presence of an odd number, setting the flag to `False` if one is found. The variable `even_exchange` is then used to determine whether an exchange can be successfully performed, with the function returning either "YES" or "NO" accordingly.