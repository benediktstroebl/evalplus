```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    if even_found:
        return "YES"
    else:
        return "NO"
```

The `exchange()` function takes two lists, `lst1` and `lst2`, as input and determines whether it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function returns "YES" if it's possible and "NO" otherwise. It uses the `any()` function with a map to check if any element in `lst1` is even. If even numbers are found in `lst1`, it returns "YES," and if none are found, it returns "NO." 

This approach ensures that the function is self-contained and doesn't rely on external variables or assumptions about the input.  It is also efficient and avoids redundant calculations as it only calls the `any()` function and the `%` operator on each element once. 

This function can be improved by incorporating a more concise algorithm, such as exploiting the list comprehension for the `any()` function, as well as integrating additional tests to validate its correctness.