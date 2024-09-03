```python
def exchange(lst1, lst2):
    even_present = any(x % 2 == 0 for x in lst1)
    if even_present:
        return "YES"
    else:
        return "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2`, as input and returns a string indicating whether it is possible to exchange elements between them to make `lst1` a list of only even numbers. The function checks if at least one even number is present in `lst1` using the `any()` function and the modulo operator to check for even numbers. If there are no even numbers in `lst1`, it returns "NO" indicating that no exchange can result in a list of only even numbers. Otherwise, it returns "YES" indicating that an exchange can be done to achieve the desired even-number-only list.