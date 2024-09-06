```python
def exchange(lst1, lst2):
    even_lst = [x for x in lst1 if x % 2 == 0]
    return "YES" if len(even_lst) != len(lst1) and all(x in lst2 for x in even_lst) else "NO"
```

The code defines a function `exchange` taking two lists `lst1` and `lst2` as input. It attempts to exchange elements between the lists to make `lst1` a list of only even numbers. It does so by creating a new list `even_lst` that contains all even numbers from `lst1`. Then it checks if the length of `even_lst` is different from the length of `lst1` and if all elements in `even_lst` are present in `lst2`. In such a case, it returns "YES," otherwise "NO."