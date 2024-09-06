```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if (arr[i] + arr[j] + arr[j + 1]) % 3 == 0:
                triples += 1
    return triples
```

The script defines a Python function `get_max_triples` that takes an integer `n` as input and returns the number of triples from the given array `arr` where `a[i] + a[j] + a[k]` is a multiple of 3. The function creates the array `arr` as stated in the problem, and then uses two nested loops to check if the sum of the elements in each triple is a multiple of 3. The `triples` counter is incremented whenever such a triple is found. The function's output is the final value of `triples`.