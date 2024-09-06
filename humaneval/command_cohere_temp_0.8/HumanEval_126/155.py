```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] != 1)
```

The function uses a simple dictionary (`dups`) to keep track of how many times each number appears in the list. If there's a duplicate number, it increments a counter; otherwise, it initializes the counter to 1. After processing all numbers, it checks if all duplicate counters equal 1, and returns `True` if so, correctly identifying the list as sorted.