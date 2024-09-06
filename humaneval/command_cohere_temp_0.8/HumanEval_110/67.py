```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    if even_found:
        return "YES"
    else:
        return "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2`, as input and checks if it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function returns "YES" if it's possible, and "NO" otherwise. This is done by using the modulo operator inside a `map` function to determine if any of the elements in `lst1` are even, and then returning the appropriate response.