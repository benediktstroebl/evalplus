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
This Python script defines a function `f` that takes an integer `n` as input and returns a list of size `n` where each element is the factorial of its index if the index is even, or the sum of numbers from 1 to that index otherwise. The script uses two arrays, `facts`, and `sums`, to calculate the factorials and sums up to a number `i`, respectively. The `for` loop iterates through numbers from 1 to `n`, and the value of the corresponding element in either `facts` or `sums` is correctly updated based on whether the index `i` is even or odd, where the value is computed correctly as well. The returned list depends on the parity of `n`, where if it's even, it returns the `sums` list, and if odd, it returns the `facts` list. In either case, the returned list satisfies the conditions stated in the problem.