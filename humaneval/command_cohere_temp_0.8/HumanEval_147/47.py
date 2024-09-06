```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum triples
    max_triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            sum_ = a[i] + a[j] + a[j + 1]
            if sum_ % 3 == 0:
                max_triples += 1
    return max_triples
```
This Python script defines a function `get_max_triples` that takes in a positive integer `n` as its input and creates an integer array `a` of length `n`, where each element `a[i]` is computed as `i * i - i + 1`. The function then returns the number of triples (`a[i]`, `a[j]`, `a[k])` where `i < j < k`, and the sum of the three array elements is a multiple of 3. To compute the number of qualifying triples, the function uses nested loops to iterate over the array and counts the number of triples that satisfy the sum-of-squares constraint. Finally, the function returns the maximum number of triples possible.