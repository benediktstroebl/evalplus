```python
def get_odd_collatz(n):
    odd_collatz = [y for y in iter_collatz(n) if y % 2 == 1]
    return sorted(odd_collatz)

def iter_collatz(n):
    yield n
    if n == 1:
        return
    if n % 2 == 0:
        yield from iter_collatz(n // 2)
    else:
        yield from iter_collatz(3 * n + 1)
```

The `iter_collatz` function is used to generate the odd numbers in the Collatz sequence for a given starting integer `n`. It uses `yield` to output only odd numbers and stops when it reaches 1, in line with the Collatz sequence definition.

The `get_odd_collatz` function encapsulates this process, immediately returning a list of all odd numbers in the Collatz sequence. This list is then sorted to ensure that the output is in increasing order. 

The list is sorted only once the generator has been exhausted and all the odd numbers in the Collatz sequence have been collected, ensuring that the process is efficient and does not consume unnecessary resources.