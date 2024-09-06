```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum triples
    triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            curr = a[i] + a[j]
            valid_ triples = curr // 3
            if curr % 3 == 0:
                triples += valid_triples
            elif curr % 3 == 1:
                triples += valid_triples - 1
            elif curr % 3 == 2:
                triples += valid_triples - 2
            # Repeat for all valid pairs (i, j)
    return triples
```

The solution is based on calculating the sum of triple values that are evenly divisible by 3, as well as 2 less than or 2 more than this number. 

To improve efficiency, it uses a single loop to iterate through all pairs of indices (`i`, `j`) and calculates the valid triples simultaneously. This reduces the complexity of the problem from O(n^3) to O(n^2). 

To achieve this, it utilizes a previously generated array `a`, where each value corresponds to the required value for the given problem. Then, it iterates through all pairs of indices, accumulating the valid triples. The result is returned by the function.