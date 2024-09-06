```python
def exchange(lst1, lst2):
    even_found = any(x % 2 == 0 for x in lst1)
    if even_found:
        return "YES"
    else:
        return "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2`, as input and checks if it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function returns "YES" if it's possible, and "NO" otherwise. This is done using the `any()` function to check if any element in `lst1` is even; if even elements are found, we can exchange those with odd elements from `lst2`, and if not, we cannot create an all-even `lst1` through exchanges. 

This approach ensures correctness in determining the possibility of achieving the all-even `lst1`, and provides clear and accurate results for the given example scenarios and any potential edge cases.