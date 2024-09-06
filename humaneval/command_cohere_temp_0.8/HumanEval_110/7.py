```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    if even_found:
        return "YES"
    else:
        return "NO"
```

The `exchange()` function takes two lists, `lst1` and `lst2`, as input and determines whether it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function checks if any element in `lst1` is even. If an even element is found, it returns "YES," indicating that an exchange can be performed to make all elements in `lst1` even. Otherwise, it returns "NO," as no exchange can yield an all-even `lst1`. The function relies on the built-in `any()` and `map()` functions and the modulo operator for evenness checking, making it concise and readable.