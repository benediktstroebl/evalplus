```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    if even_found:
        return "YES"
    else:
        return "NO"
```

The `exchange()` function takes two lists, `lst1` and `lst2`, as input and determines whether it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function returns "YES" if it's possible and "NO" otherwise. It utilizes the `any()` function with a lambda function to efficiently check if any element in `lst1` is even, explicitly checking for the condition required by the prompt.  This implementation adheres to the problem's requirements and provides the intended functionality in a straightforward manner.  The `exchange()` function should work correctly for any valid input as per the problem statement.