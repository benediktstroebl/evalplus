```python
def exchange(lst1, lst2):
    even_numbers = [x for x in lst1 if x % 2 == 0]
    if len(even_numbers) == len(lst1):
        return "YES"
    else:
        return "NO"
```

The `exchange()` function takes two lists, `lst1` and `lst2`, as input and checks if it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function first creates a list called `even_numbers` that contains all the even numbers from `lst1`. Then, it checks if the length of `even_numbers` is equal to the length of `lst1`. If they have the same length, it returns "YES," indicating that all elements in `lst1` can be even. If not, it returns "NO," indicating that not all elements in `lst1` can be even. This function utilizes list comprehension and basic logic to solve the problem. 

The problem assumes that the input lists will be non-empty, and there is no limitation on the number of exchanged elements between the two lists. Thus, this function optimally solves the problem without any time complexity issues for any number of elements or constraints.