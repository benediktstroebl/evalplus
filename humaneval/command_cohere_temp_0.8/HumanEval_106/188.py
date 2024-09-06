```python
def f(n):
    facts = [0] * n
    sums = [0] * n
    for i in range(1, n+1):
        facts[i] = facts[i - 1] * i
        if i % 2 == 0:
            sums[i] = sums[i - 1] + i
    return facts + sums
```
This Python script defines the `f` function, as per the specification in the markdown code block. It initializes two arrays, `facts` and `sums`, both with initial values of 0 for all indices up to `n`. It then iterates through the indices from 1 to `n` (inclusive) and populate the `facts` array with the factorial of each even index, and the `sums` array with the sum of numbers from 1 to each odd index. The final value of the `facts` and `sums` arrays is returned, respectively, giving the desired output.