```python
def tri(n):
    prev = [3, 1]
    result = []
    while len(result) < n + 1:
        if len(result) % 2 == 0:
            result.append(prev[-1] + prev[-2] + int(prev[-1] / 2))
        else:
            result.append(prev[-1] + prev[-2] + prev[-3])
        prev.append(result[-1])
    return result[:n+1]
``` 

The code defines a recursive function `tri(n)` that generates the `n+1` first terms of the Tribonacci sequence, based on the problem statement and auxiliary equations provided. It maintains an even or odd balance to determine whether the next term is calculated using the recurrence relation `1 + n/2` or the sum of the previous three terms. The result list is initialized, and terms are added until it contains `n+1` elements. The output is then trimmed to return the first `n` terms requested, and examples provided in the problem showcase its behavior.