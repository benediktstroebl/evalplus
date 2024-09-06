```python
def get_odd_collatz(n):
    odd_seq = [x for x in map(lambda x: x if x % 2 else x * 2, collatz_iter(n)) if x % 2 == 1]
    return sorted(odd_seq)

def collatz_iter(n):
    yield n if n == 1 else (yield n)
    yield from collatz_iter(n // 2 if n % 2 else n * 3 + 1)
```

The `collatz_iter` function is used to generate the collatz sequence for a given input `n` and uses recursion with a generator expression to keep iterating over the sequence. Then, the `get_odd_collatz` function filters out odd numbers from the collatz sequence and returns them sorted. The generator expression in the `map` function is used to transform even numbers to their half and keeps odd numbers as is.