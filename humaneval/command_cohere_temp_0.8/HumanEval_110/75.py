```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    if even_found:
        return "YES"
    else:
        return "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2`, as input and determines whether it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function returns "YES" if it's possible and "NO" otherwise. This determination is made based on whether an even number is found in `lst1`, using the `any()` function with a map lambda function to check if any element in `lst1` is even. If an even number is found, it returns "YES," and if none is found, it returns "NO." 

This approach ensures that if any even numbers are found in `lst1`, they can be exchanged with odd numbers from `lst2`, and if no even numbers are found in `lst1`, it is impossible to exchange elements from `lst2` to achieve the desired result, given that the input lists are assumed to be non-empty. 

This problem can be solved using Python's list and boolean manipulation capabilities, which the provided code illustrates.