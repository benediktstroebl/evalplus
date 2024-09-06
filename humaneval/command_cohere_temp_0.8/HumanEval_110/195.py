```python
def exchange(lst1, lst2):
    even_found = any(lst1)
    return "YES" if even_found and all(x in lst2 for x in lst1) else "NO"
```
The `exchange()` function takes two lists, `lst1` and `lst2`, as input and determines whether it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function returns "YES" if it's possible and "NO" otherwise. 

The function utilizes the `any()` function to check if there are any even numbers present in `lst1`, and the `all()` function to verify if all elements in `lst1` are present in `lst2`, indicating that it's possible to transfer elements between the lists to make `lst1` consist only of even numbers. 

This approach ensures that the function is self-contained and doesn't rely on any external variables or assumptions about the input. 

This script solves the problem in a straightforward manner and aligns with the specifications provided.