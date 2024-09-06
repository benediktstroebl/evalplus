```python
def f(n):
    facts = [0] * n
    sums = [0] * n
    for i in range(1, n+1):
        facts[i-1] = i if i % 2 == 0 else 1
        sums[i-1] = i if i % 2 != 0 else sum(range(1, i+1))
    return facts + sums
```
This Python script defines the `f` function, as specified in the problem statement. It generates a list where the even indices hold the factorials of those indices and the odd indices hold the sum of numbers from 1 to that index. This is achieved through the `facts` and `sums` lists, with the `range` generator creating the necessary indices from 1 to `n`. The two lists are then concatenated and returned to fulfill the problem requirement.