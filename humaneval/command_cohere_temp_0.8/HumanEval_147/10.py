```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate max triples
    triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if (a[i] + a[j] + a[j + 1]) % 3 == 0:
                triples += 1
    return triples
```

This script creates the sequence of numbers as described in the prompt and then iterates through all possible pairs of values except the largest value, checking whether the sum of the three values is a multiple of 3. This is counted as a triple, and the total number of qualifying triples is returned. 

The `triples` variable is incremented each time a triplet is found. 

The code does not rely on any global variables, making it a self-contained solution. 

The `get_max_triples` function should work correctly for the given input of `n = 5`, as per the example in the prompt, resulting in the output of `1`.