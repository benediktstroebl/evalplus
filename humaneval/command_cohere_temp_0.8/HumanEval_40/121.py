```python
def triples_sum_to_zero(lst):
    # Write your code here. Read the markdown for more details.
    return len(set(zip(lst, lst[1:], lst[2:] + [None]))) == 3 and all(a + b + c == 0 for a, b, c in zip(lst, lst[1:], lst[2:] + [None]))
```

Using set comprehension and `zip`, we group the list into three elements at a time.
We then check if there are exactly three distinct groups and if each group sums to zero.