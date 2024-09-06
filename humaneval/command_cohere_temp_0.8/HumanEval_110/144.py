```python
def exchange(lst1, lst2):
    even_found = any(x % 2 == 0 for x in lst1)
    if even_found:
        return "YES"
    else:
        return "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2`, as input and returns a string indicating whether it is possible to exchange elements between them to make `lst1` a list of only even numbers. The function checks if any element in `lst1` is even and returns a "YES" string if true, indicating that an even number is present and can be swapped with an odd number from `lst2`. If no even numbers are found in `lst1`, the function returns a "NO" string, indicating that no even numbers can be swapped from `lst2` to make `lst1` all even. 

This approach eliminates the need to explicitly manipulate the lists and instead focuses on evaluating the criteria directly using Python's built-in functionalities.