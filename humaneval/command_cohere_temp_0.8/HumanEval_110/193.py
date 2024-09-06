```python
def exchange(lst1, lst2):
    even_present = any(x % 2 == 0 for x in lst1)
    if even_present:
        return "YES"
    else:
        return "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2`, as input and returns a string indicating whether it is possible to exchange elements between them to make `lst1` a list of only even numbers. The function checks if any element in `lst1` is even and directly returns "YES" if any element is even. It returns "NO" if all elements in `lst1` are odd, indicating that an even number cannot be formed. This function solves the problem without modifying the original lists, as required.