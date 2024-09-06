```python
def exchange(lst1, lst2):
    even_found = any(x % 2 == 0 for x in lst1)
    if even_found:
        return "YES"
    else:
        return "NO"
```

The `exchange()` function takes two lists, `lst1` and `lst2`, as input and determines whether it is possible to exchange elements between them to make `lst1` a list of only even numbers. The function examines whether an even number is present inside `lst1` with the use of the `any()` function and a `lambda` expression, which determines if any element in `lst1` is even. If even, the function returns "YES" indicating that an exchange can be achieved. If no even numbers are found in `lst1`, then the function returns "NO" indicating that no exchange can make `lst1` contain only even numbers. 

This approach ensures that the exchange can be achieved by swapping elements between the two lists, and it is concise and easy to understand.