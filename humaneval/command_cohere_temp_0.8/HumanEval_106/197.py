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
This Python script defines a function `f` that takes an integer `n` as input and creates two lists: `facts` and `sums`, which calculate the factorials of even indices and the sums of natural numbers up to odd indices, respectively. The `if` statement determines whether the result should be based on facts or sums, relying on the parity of `n`. This approach efficiently generates the required list of values.