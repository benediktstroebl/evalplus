```python
def exchange(lst1, lst2):
    even_index = [i for i, n in enumerate(lst1) if n % 2 == 0]
    if len(even_index) != len(lst1):
        return "NO"
    lst1_copy = [element for element in lst1]
    for idx in even_index:
        lst1[idx] = lst2[idx]
    for idx, element in enumerate(lst2):
        if element % 2 == 0:
            lst1[idx] = lst1_copy[idx]
            return "YES"
    return "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2`, as its input. First, it creates an index list of even numbers in `lst1` using a list comprehension and checks if the length of this list is equal to the length of `lst1`, and if so, it proceeds to swap the even numbers in `lst1` with their corresponding numbers in `lst2`. Afterward, it checks if any of the elements in `lst2` has been swapped; if so, it returns "YES," indicating that the exchange was successful. If not, it returns "NO," indicating that the exchange was not successful.