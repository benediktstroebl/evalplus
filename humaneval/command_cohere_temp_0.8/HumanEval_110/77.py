```python
def exchange(lst1, lst2):
    even_found = any(x % 2 == 0 for x in lst1)
    if even_found:
        return "YES"
    else:
        return "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2`, as input and determines whether it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function returns "YES" if it's possible and "NO" otherwise. This determination is done simply by checking if any element in `lst1` is even, by using the `any()` function and testing for evenness with the modulo operator (`x % 2 == 0`). 

This is the essence of the solution, which is nicely packaged in a single function for easy usage anywhere. 

NOTE: This solution assumes the input lists will be non-empty, as stated in the problem statement. If this is not the case, the solution may not work as expected.