```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate the maximum triples
    triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            sum_ = a[i] + a[j] + a[j + 1]
            if sum_ % 3 == 0:
                triples += 1
    return triples
```

The problem is solved by generating the array `a` as required in the prompt. The nested loops are used to iterate through all eligible pairs of elements and check whether the sum of the third element (`a[j + 1]`) together with the sum of the two chosen elements is a multiple of 3. The code is modular and efficient, with a time complexity of `O(n^2)`. It should be noted that the maximal triple counting can be improved by removing the nested loops.