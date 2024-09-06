```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum triples
    # Consider all possible combinations of size 3 from the sequence
    # And count the valid ones (where the sum is divisible by 3)
    max_triples = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            valid = False
            for k in range(j+1, n+1):
                if a[i] + a[j] + a[k] % 3 == 0:
                    valid = True
                    break
            if valid:
                max_triples += 1
    return max_triples
```

The approach is to iterate through all possible pairs of the array `a` and then iterate through all possible indices of the third element in the array. Additionally, check whether their sum is a multiple of 3. This can be achieved with a nested for loop. However, it is important to ensure that the indices `i`, `j`, and `k` are selected in a way that ensures `i < j < k`.