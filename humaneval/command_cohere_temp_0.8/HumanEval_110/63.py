```python
def exchange(lst1, lst2):
    even_found = any(x % 2 == 0 for x in lst1)
    if even_found:
        return "YES"
    else:
        return "NO"
```

The `exchange()` function takes two lists, `lst1` and `lst2`, as input. It checks if any element in `lst1` is even. If any even number is found, it returns "YES," indicating that an exchange can be performed to make all elements in `lst1` even. If no even numbers are found in `lst1`, it returns "NO," indicating that no possible exchange can make all elements in `lst1` even.