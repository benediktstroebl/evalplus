```python
def get_odd_collatz(n):
    odd_collatz = [x for x in collatz(n) if x % 2 != 0]
    return sorted(odd_collatz)

def collatz(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return collatz(n // 2) + [n // 2]
    else:
        return collatz(3 * n + 1) + [3 * n + 1]
```

The `collatz` function uses recursion to generate the Collatz sequence. If `n` is 1, it returns [1]; if `n` is even, it divides `n` by 2 and adds that value to the sequence; if `n` is odd, it multiplies `n` by 3, adds 1, and adds that value to the sequence. The `get_odd_collatz` function filters out the odd numbers from the sequence and sorts them in ascending order.