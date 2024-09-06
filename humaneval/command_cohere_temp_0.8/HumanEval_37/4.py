```python
def sort_even(l: list):
    even = [e for e in l if e % 2 == 0]
    odd = [o for o in l if o % 2 != 0]
    return even + sorted(odd)
```

This Python script defines a function `sort_even` that solves the problem as outlined in the prompt. It first identifies the even and odd indices of the list, using list comprehensions to separate them into `even` and `odd` lists. The `sorted` function is then used to sort the values in the `odd` list, and the sorted `odd` list is concatenated with the `even` list to create the final `l'` list. This approach ensures that the odd indices retain their original values, while the even indices are sorted as described in the problem statement.