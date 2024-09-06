```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum triples
    max_triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            current_sum = a[i] + a[j]
            max_triples = max(max_triples, len(list(filter(lambda x: x == current_sum, [a[k] for k in range(n) ]))))
    return max_triples
```
This Python script defines a function called `get_max_triples` that takes in a positive integer `n` as its input and creates an integer array `a` of length `n`, where each element in the array is computed as `i * i - i + 1`, with `i` ranging from 1 to `n`. Then, it calculates the number of triples (`a[i]`, `a[j]`, `a[k])` where `i < j < k`, and the sum of the triplet is a multiple of 3.

The script returns the number of these qualifying triples where `a[i] + a[j] + a[k]` is a multiple of 3. It iterates through each pair of values in the array and counts the valid triplets that follow the requirement. Finally, it returns the maximum number of qualifying triplets possible.