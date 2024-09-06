```python
def exchange(lst1, lst2):
    even_occurring = any(x % 2 == 0 for x in lst1)
    if even_occurring and all(x % 2 == 0 for x in lst2):
        return "YES"
    return "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2` as input and returns a string indicating whether the even numbers from `lst2` can be exchanged with the odd numbers from `lst1` to result in a list of only even numbers in `lst1`. The function checks if there are any even numbers in `lst1` and if all the numbers in `lst2` are even. If both conditions are met, it returns "YES," indicating that an even number exchange is possible. Otherwise, it returns "NO," indicating that no such exchange is possible.