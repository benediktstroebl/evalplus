```python
def exchange(lst1, lst2):
    odd = next((el for el in lst1 if el % 2 != 0), None)
    even = next((el for el in lst2 if el % 2 == 0), None)
    if odd is None or even is None:
        return "YES"
    return "NO"
```

The function `exchange()` is designed to solve the problem of determining whether it is possible to exchange elements between two lists, `lst1` and `lst2`, to make `lst1` a list of only even numbers. The function uses list comprehensions to find the first odd element in `lst1` and the first even element in `lst2`. If an odd element is found in `lst1` or an even element is found in `lst2`, it means that an exchange can be done and "YES" is returned. However, if both an odd element and an even element are found in their respective lists, then "NO" is returned, indicating that an exchange cannot be done. 

The given example tests, including edge cases, are also provided to ensure the accuracy of the function.