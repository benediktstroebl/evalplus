```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize the count of triples
    max_triples = 0
    
    # Consider all possible triples
    for i in range(n-2):
        for j in range(i+1, n-1):
            k = range(j+1, n)
            rem = a[i] + a[j] + a[k[0]]
            if rem % 3 == 0:
                max_triples += 1
    
    return max_triples
```

This script creates the array `a` as described in the prompt, and then iterates through all possible pairs of elements, checks whether the third required element is a multiple of 3 when added to the two selected elements, and counts valid triples accordingly. As the nested loops iterate through all elements, the result should be the correct maximum number of triples satisfying the problem's criteria.