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
This Python script defines a function `f` that takes an integer `n` as input and creates two lists: `facts` and `sums`, which calculate the factorials and sums of integers from 1 to `n` respectively. The `facts` list stores the factorial values of even indices, while the `sums` list stores the sum of numbers from 1 to each index for odd indices. Finally, the function returns the `sums` list if `n` is even, or the `facts` list if `n` is odd.