```python
def exchange(lst1, lst2):
    even_present = any(x % 2 == 0 for x in lst1)
    if even_present:
        return "YES"
    else:
        return "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2`, as input and returns a string indicating whether it is possible to exchange elements between them to make `lst1` a list of only even numbers. The function first checks if any element in `lst1` is even; if any is, it returns "YES"; otherwise, it returns "NO". This is done using the `any()` function and testing if each element in `lst1` is divisible by 2, using the modulo operator (`%`). 

This solution allows you to perform the exchange of elements between the two lists, assuming no element is repeated in both lists and requires no extra storage, as it doesn't require building any new lists from either input list. 

It is important to note, however, that this function assumes no element in either list is repeated.