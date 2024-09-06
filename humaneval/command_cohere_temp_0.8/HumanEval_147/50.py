```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Initialize variables to track triples and multiples of three
    triples = 0
    multiple_of_three = 0
    
    # Calculate multiples of three and triples
    for i in range(n - 2):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                if a[i] + a[j] + a[k] % 3 == 0:
                    triples += 1
                if a[i] + a[j] + a[k] % 3 == 0:
                    multiple_of_three += 1
    
    return triples
```

This script creates the sequence a as per the prompt, and then iterates through all possible pairs of elements to count the triples and tally multiples of three. It then returns the number of triples as the final output. The function optimally solves the problem without iterative approaches that might require pruning or memoization.