```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [1] + [n // 2] * (n // 2)
    else:
        prev = [0, 1, 3]
        curr = [0, 1, 3]
        next = [0, 1, 3]
        for _ in range(n - 2):  # iterate n - 2 times
            temp = [prev[i] + curr[i] + next[i] for i in range(3)]
            prev, curr, next = curr, next, temp
        return [prev[i] for i in range(n + 1)]
```

The function employs an iterative approach to generate the Tribonacci sequence by keeping track of the last three terms (prev, curr, and next). It employs a temporary list `temp` to store the sum of the previous three terms, updating `prev`, `curr`, and `next` accordingly. Finally, it returns the last `prev` list, which contains the first `n + 1` numbers of the Tribonacci sequence.