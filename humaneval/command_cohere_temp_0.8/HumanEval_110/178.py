```python
def exchange(lst1, lst2):
    odd = lst1.count(2)
    even = lst2.count(2)
    if odd == 0 and even > 0:
        return "YES"
    return "NO"
```

This Python script defines a function `exchange` that takes two lists `lst1` and `lst2` as input. It checks whether it is possible to exchange elements between the two lists to make `lst1` contain only even numbers. It does so by counting the number of odd numbers in `lst1` and the number of even numbers in `lst2`. If there are no odd numbers in `lst1` (i.e., they can all be exchanged with even numbers from `lst2`), and there are still some even numbers remaining in `lst2`, it returns "YES." Otherwise, it returns "NO" indicating that no possible exchange can be done to make lst1 contain only even numbers. 

This solution employs a simple counting strategy to determine if the exchange is feasible and provides a clear yes/no outcome. It is adaptable to various scenarios because the exchange procedure can be completed in a single iteration.