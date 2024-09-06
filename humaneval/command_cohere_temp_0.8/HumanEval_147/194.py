```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate the maximum triples result
    max_triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            current_sum = a[i] + a[j]
            if current_sum % 3 == 0:
                max_triples += 1
    return max_triples
```

The script uses nested loops to iterate through all possible pairs of arrays elements between different indices and calculates the sum of these elements. If the sum is evenly divisible by 3, it adds 1 to the `max_triples` variable, which is later returned as the result.

Make sure to have a standalone function designated to solve the problem statement to perfectly match the criteria of a self-contained code block.