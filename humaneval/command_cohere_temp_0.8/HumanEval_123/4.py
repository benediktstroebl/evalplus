```python
def get_odd_collatz(n):
    odd_collatz = [1]
    while n != 1: 
        if n % 2 == 1: 
            odd_collatz.append(n)
        if n % 2 == 0: 
            n = n // 2
        else: 
            n = 3 * n + 1
    odd_collatz.sort()
    return odd_collatz
```

The `get_odd_collatz` function uses a straightforward iterative approach to construct the odd numbers in the Collatz sequence for a given starting integer `n`. It begins with `odd_collatz` containing only 1 and iteratively updates `n` following the Collatz sequence rules. When `n` reaches 1, the loop ends, and the odd numbers collected are sorted and returned. The function meets the given requirements and outputs a list of odd numbers in the Collatz sequence for any positive integer input.