Here is a Python script that solves the given problem:
```python
def f(n):
    facts = [0] * n
    sums = [0] * n
    for i in range(1, n+1):
        facts[i-1] = i if i % 2 == 0 else 1
        sums[i-1] = i if i % 2 == 0 else sum(range(1, i+1))
        
    return facts if n % 2 == 0 else sums
```
This script defines a function f that takes an input n and returns a list according to the specification. The function creates two parallel lists, `facts` and `sums`, where `facts[i]` holds the ith factorial value for even indices, and `sums[i]` holds the sum of numbers from 1 to ith index for odd indices. The loop iterates from 1 to n, calculating the factorial and sum values simultaneously, with the final result list being a combination of the `facts` and `sums` lists based on the parity of the input n.