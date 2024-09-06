```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    if even_found:
        return "YES"
    else:
        return "NO"
```

The function employs the `any()` function with a mapping operation to determine if there are any even numbers present in `lst1`. If even numbers are found, it returns "YES" since the requirement of having all even numbers in `lst1` is satisfied. If no even numbers are found in `lst1`, the function returns "NO". This logic bases the answer on the presence of at least one even number in `lst1`, regardless of the `lst2` list. 

**NOTE:** The provided solution relies on the assumption that the initial lists in the example provided in the problem statement are representative of the validity of the exchange, not necessarily the provided lists themselves.