```python
def exchange(lst1, lst2):
    even_occurrences = sum(x % 2 == 0 for x in lst1)
    return "YES" if even_occurrences == len(lst1) else "NO"
```

The function `exchange()` checks if it's possible to exchange elements between `lst1` and `lst2` to make `lst1` a list of only even numbers. It does so by counting the occurrences of even numbers in `lst1` with the line `even_occurrences = sum(x % 2 == 0 for x in lst1)`. If this count is equal to the length of `lst1`, then `lst1` only contains even numbers, meaning the answer is "YES". Otherwise, the answer is "NO". This solution incorporates the specified requirement that the input lists are assumed to be non-empty.