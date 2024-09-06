```python
def f(n):
    facts = [0] * n
    sums = [0] * n
    for i in range(1, n+1):
        facts[i] = facts[i - 1] * i
        if i % 2 == 1:
            sums[i] = sums[i - 1] + i
    return facts + sums
```
This Python script defines the `f` function, as requested, using two nested lists (`facts` and `sums`) and list comprehensions to calculate the factorials and sums of numbers from 1 to `n` `(`inclusive`)` and assign them to the corresponding list elements. This allows the function to return the requested list of size `n` with alternating factorials and sums of numbers from 1 to `i`, as specified in the problem statement.