```python
def exchange(lst1, lst2):
    even_found = any(x % 2 == 0 for x in lst1)
    if even_found:
        return "YES"
    else:
        return "NO"
```

The `exchange()` function takes two lists, `lst1` and `lst2`, as input. It checks if any element in `lst1` is even. If any even numbers are found in `lst1`, it returns "YES" since we can exchange any number of elements between the two lists to make `lst1` all even numbers. If no even numbers are found in `lst1`, it returns "NO" since exchanging elements won't make all the elements in `lst1` even.

This approach takes advantage of the simplicity of Python's built-in functions and the any function in particular to easily check for the presence of even numbers in `lst1`.