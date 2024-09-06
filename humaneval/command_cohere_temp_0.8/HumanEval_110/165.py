```python
def exchange(lst1, lst2):
    even_found = any(lst1)
    return "YES" if even_found else "NO"
```

The `exchange()` function takes two lists, `lst1` and `lst2`, as input and determines whether it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function returns "YES" if it's possible and "NO" otherwise. This determination is achieved by using the `any()` function to check if `lst1` contains at least one even number. If any even number is found in `lst1`, the `exchange()` function returns "YES," assuming that we can exchange at least one even number with an odd number from `lst2`. If no even numbers are found in `lst1`, meaning it contains only odd numbers, the function returns "NO," as no possible exchange can result in a list of only even numbers.