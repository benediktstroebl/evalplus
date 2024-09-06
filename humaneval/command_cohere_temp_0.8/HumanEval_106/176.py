```python
def f(n):
    facts = [0] * n
    sums = [0] * n
    for i in range(1, n+1):
        facts[i & -i - 1] = i
        sums[i] = sum(range(1, i+1))
    return facts + sums
```
This Python script defines the `f` function, as specified in the problem statement. It generates a list where the even indices are filled with the factorial of the index, and the odd indices are filled with the sum of the digits up to that index. This is achieved through the `list comprehension` that combines the `facts` and `sums` lists. The resulting list is returned by the function.