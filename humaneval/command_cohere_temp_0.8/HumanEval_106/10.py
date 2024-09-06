```python
def f(n):
    facts = [0] * n
    sums = [0] * n
    for i in range(1, n+1):
        facts[i] = facts[i - 1] * i
        if i % 2 == 0:
            sums[i] = sums[i - 1] + i
    return sums if n % 2 == 0 else facts
```
This Python script defines a function `f` that takes an integer `n` as input and returns a list of size `n` where each element is either the factorial of an even index or the sum of numbers from 1 to an odd index, starting from index 1. The script initializes two lists, `facts` and `sums`, both of size `n`, to store the factorials and sums up to index `n`. It then uses a loop to calculate these values iteratively for each index up to `n`. If `n` is even, it returns the `sums` list, and if `n` is odd, it returns the `facts` list.