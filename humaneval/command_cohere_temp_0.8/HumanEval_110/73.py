```python
def exchange(lst1, lst2):
    even_found = any(x % 2 == 0 for x in lst1)
    if even_found:
        return "YES"
    else:
        return "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2`, as input and checks if it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function returns "YES" if it's possible, and "NO" otherwise. This is done using the `any()` function to check if any element in `lst1` is even; if at least one even element is in `lst1`, the exchange can happen and the function returns "YES." If not, it returns "NO."