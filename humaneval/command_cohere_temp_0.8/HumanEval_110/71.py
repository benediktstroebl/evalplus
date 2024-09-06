```python
def exchange(lst1, lst2):
    even_found = any(lst1)
    return "YES" if even_found and all(x in lst2 for x in lst1) else "NO"
```
The `exchange()` function takes two lists, `lst1` and `lst2`, as input and determines whether it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function first checks if there are any even numbers in `lst1` using the `any()` function. If there are no even numbers, then it returns "NO" since no exchange can result in a list of only even numbers. If there is at least one even number in `lst1`, it checks if all the elements in `lst1` are present in `lst2` using the `all()` function. If this condition is met, it means elements can be exchanged to make `lst1` a list of only even numbers, and the function returns "YES." Otherwise, it returns "NO."