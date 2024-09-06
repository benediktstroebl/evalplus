```python
def f(n):
    facts = [0] * n
    sums = [0] * n
    for i in range(1, n+1):
        facts[i-1] = i if i % 2 == 0 else 1
        sums[i-1] = i if i % 2 != 0 else sum(range(1, i+1))
    return facts + sums
```
This Python script defines the `f` function, as requested, using two lists to store the respective results, then utilizing a loop to calculate the values accordingly. This approach cleanly separates the two types of problems and should provide a clear pathway to adapt the code to future changes. It also allows for parallel operations to improve performance if needed.