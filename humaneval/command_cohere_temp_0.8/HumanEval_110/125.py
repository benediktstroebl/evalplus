```python
def exchange(lst1, lst2):
    even_found = any(lst1)
    return "YES" if even_found else "NO"
```
The `exchange()` function takes two lists, `lst1` and `lst2`, as input. It determines whether it's possible to exchange elements between these two lists to make `lst1` contain only even numbers. This determination is done through the use of the `any()` function, which checks if any element in `lst1` is even. If any even number is found in `lst1`, it's possible to exchange elements with `lst2` to end up with an all-even `lst1`, and thus the function returns "YES." Otherwise, if no even numbers are found in `lst1`, it's not possible to achieve such an exchange, and the function returns "NO." 

This approach doesn't explicitly exchange elements but rather leverages the fact that Python's `any()` function returns `True` as soon as it encounters an even number. Thus, if any even numbers are present in `lst1`, it's possible to refine `lst1` into an all-even list through exchanges, and vice versa.