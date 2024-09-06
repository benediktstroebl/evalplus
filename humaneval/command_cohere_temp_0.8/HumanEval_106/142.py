```python
def f(n):
    facts = [0] * n
    sums = [0] * n
    for i in range(1, n+1):
        facts[i] = facts[i - 1] * i
        if i % 2 == 1:
            sums[i] = sums[i - 1] + i
    return sums if n % 2 == 0 else facts
```
This Python script defines a function 'f' that solves the described problem. It creates two lists, 'facts,' which will hold the factorials of even indices, and 'sums,' which will hold the sums of numbers from 1 to odd indices. The script then iterates through indices from 1 to 'n,' calculating the factorial for even indices and the sum for odd indices, using a preallocated list to store these values. The function then returns the 'sums' list if the 'n' is even, rendering the list of factorials; otherwise, it returns the 'facts' list, yielding the list of cumulative sums. This functionality is highlighted in the example usage provided in the original problem statement.