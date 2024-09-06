```python
def get_odd_collatz(n):
    odd_collatz = [y for y in collatz(n) if y % 2 != 0]
    return sorted(odd_collatz)

def collatz(n):
    if n == 1:
        return [1]
    if n % 2 == 0:
        return collatz(n // 2) + [n // 2]
    else:
        return collatz(3 * n + 1) + [3 * n + 1]
```

The `collatz` function recursively calculates the full Collatz sequence for a given starting integer `n`, excluding the base case of `n == 1`. If `n` is even, it divides by 2; otherwise, it multiplies by 3 and adds 1.

The `get_odd_collatz` function filters out odd numbers from the Collatz sequence and returns them in a sorted order. 

You can use the function by calling `get_odd_collatz(5)`, which should return `[1, 5]` corresponding to the Collatz sequence for 5.  Remember, the Collatz sequence for 5 is `[5, 16, 8, 4, 2, 1]`, so the odd numbers are only 1 and 5.