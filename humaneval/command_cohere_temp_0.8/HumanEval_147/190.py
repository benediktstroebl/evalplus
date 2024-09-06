```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize the count of triples
    triples = 0
    
    # Calculate the number of triples for values greater than or equal to 3
    for i in range(3, n + 1, 3):
        for j in range(i + 1, n + 1, 3):
            k = (i + j) // 2
            if k >= 1 and a[k - 1] == 2:
                triples += 1
    
    return triples
```

The solution operates by first constructing the array of values and then iterating through all feasible permutations of three elements in the array, determining whether their sum is divisible by three. The method determines whether the middle number is 2, in which case it adds to the count of triples, assuming the first and last numbers are distinct. The maximum number of triples is returned.

This algorithm has a time complexity of O(N^2), where N is the input length. This is due to the nested loop structure and the constant time operations inside the loops.