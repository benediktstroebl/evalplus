```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum triples
    max_triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            current_sum = a[i] + a[j]
            triples = (current_sum - 1) // 3
            max_triples = max(max_triples, triples)
    return max_triples
```
This script creates the array needed for the parameters that are provided and then calculates the maximum number of triples using both nested loops. The number of triples is calculated by determining the number of divisions that are able to be made by the sum of the two elements within the array, which is then converted by subtracting one and dividing by three to provide the appropriate number of triples. This number is then returned to the caller.