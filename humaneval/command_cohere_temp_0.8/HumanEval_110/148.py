```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    if even_found:
        return "YES"
    else:
        return "NO"
```

The function employs the `any()` function with a mapping operation to quickly ascertain whether `lst1` contains any even numbers, by evaluating each number in the list to determine if it's even. Subsequently, it returns either "YES" or "NO" based on this determination, solving the problem efficiently.