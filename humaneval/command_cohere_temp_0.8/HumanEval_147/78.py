```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] + arr[j-i-1]) % 3 == 0:
                triples += 1
    return triples
```
This Python script defines a function called `get_max_triples` that takes in a positive integer `n` as its input. This function creates an integer array `a` of length `n`, where each element `a[i]` is computed as `i * i - i + 1` (this is a triangular number triangle). The task is to return the number of unique triples (a[i], a[j], a[k]) where `i < j < k`, and `a[i] + a[j] + a[k]` is a multiple of 3. The function accomplishes this by counting the number of triples that satisfy this condition, and returns this count.