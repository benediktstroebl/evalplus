```python
def tribonacci(n):
    result = [0,1,3]
    if n<=0:
        return []
    while len(result) < n + 1:
        num = 1 if result[-1] == 0 else 0
        if len(result) % 2 == 0:
            num += result[-1]
            num += result[-2]
        else:
            num += int(result[-1] + result[-2] + result[0])
        result.append(num)
    return result[:n+1]
```

The function creates an initial list with the first two elements of the Tribonacci sequence and then iteratively computes the subsequent elements, complying with the definition of the Tribonacci sequence. The generated list is then trimmed to `n+1` elements and returned.