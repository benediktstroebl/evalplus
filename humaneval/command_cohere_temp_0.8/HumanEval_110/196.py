```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    if even_found:
        return "YES"
    else:
        return "NO"
```

The `exchange()` function takes two lists, `lst1` and `lst2`, as input and determines whether it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function returns "YES" if it's possible and "NO" otherwise. It uses the `any()` function with a lambda function to check if any element in `lst1` is even, and accordingly returns the appropriate response. 

This approach ensures that the function is self-contained and doesn't rely on external variables or assumptions about the input.