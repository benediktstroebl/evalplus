```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [0, 1, n // 2]
    else:
        return [tribonacci(n - 1)[-1:] + [tribonacci(n - 2)[-1:] + [tribonacci(n + 1)[-1:]] for _ in range(n // 2 + 1)]
```
The function creates an iterable containing the Tribonacci sequence with the last element duplicated such that the length is n + 1. It has an initial case for n == 1, and for n even it calculates the middle element, then adds 1 and 0 at the beginning. For n odd, it iterates through even values from 2 to n, recursively calculating each element as the sum of the previous two elements in the sequence, with the initial case for n == 1.