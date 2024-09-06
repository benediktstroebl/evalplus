```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize counter
    max_triples = 0
    
    # Calculate the number of triples that satisfy the condition
    for i in range(n-2):
        for j in range(i+1, n-1):
            if (a[i] + a[j] + a[j+1]) % 3 == 0:
                max_triples += 1
    
    return max_triples
```

The script uses a generator expression to create the sequence `a` in the code. The logic then iterates over unique pairs of indices to check whether the sum of the corresponding array elements is divisible by 3. The resulting counter is returned as the solution. 

This solution is efficient and can handle large inputs due to the inherent properties of the sequence `a` which is generated. 

The time complexity is O(n^2) due to the nested loop, but the code can be optimized further using the properties of the sequence `a`.