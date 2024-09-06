```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    count_diff_odd = sum(x % 2 != y % 2 for x, y in zip(lst1, lst2))
    return "YES" if even_found and count_diff_odd >= len(lst1) // 2 else "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2`, as input and returns a string indicating whether it is possible to exchange elements between them to make `lst1` a list of only even numbers. The function checks if at least one even number is present in `lst1` with the line `even_found = any(map(lambda x: x % 2 == 0, lst1))`. It counts the difference of odd and even numbers between the elements of `lst1` and `lst2` exchanged, using the sum function and a generator expression, `count_diff_odd = sum(x % 2 != y % 2 for x, y in zip(lst1, lst2))`. The condition `count_diff_odd >= len(lst1) // 2` checks if the number of odd numbers exchanged between the lists is enough to turn all the numbers in `lst1` into even numbers, given that at least one even number is already in `lst1`. The function returns "YES" in this case; otherwise, it returns "NO".