```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    # Calculate the maximum number of triples
    max_triples = sum(1 for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n) if arr[i] + arr[j] + arr[k] % 3 == 0)
    return max_triples
```
The solution is to iterate through all possible triples (i, j, k) and count those where `arr[i] + arr[j] + arr[k] ` is a multiple of 3. This can be achieved with three nested loops.

However, please note that this solution is inefficient and can time out for larger values of `n`. This is because the nested loops result in `n * (n - 1) * (n - 2) / 6` iterations at most, which is not enough for larger `n` as it will exceed the maximum execution time for some programming environments.

There are more efficient ways to solve this problem, such as sorting the array and using two pointers, that reduce the number of iterations required to count the valid triples. If desired, I can provide a revised solution.