```python
def exchange(lst1, lst2):
    even_present = any(num % 2 == 0 for num in lst1)
    if even_present:
        return "YES"
    else:
        return "NO"
```

The `exchange()` function takes two lists, `lst1` and `lst2`, as input and determines whether it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function returns "YES" if it's possible and "NO" otherwise. This determination is made based on whether an even number is already present in `lst1`, by using the `any()` function and a `num % 2 == 0` condition. Thus, the logic assesses whether an exchange could result in a list of all even numbers without explicitly swapping elements, making it more efficient.