```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize the count of triples
    triples = 0
    
    # Calculate valid triples and count them
    for i in range(n-2):
        for j in range(i+1, n-1):
            if (a[i] + a[j] + a[j+1]) % 3 == 0:
                triples += 1
    
    return triples
```

This script creates the array `a` as described in the problem statement. It then calculates the valid triples using two nested loops and counts them. To test this function, you can call it with an argument and print the result, as demonstrated in the following code:
```python
# Test the function
n = 5
max_triples = get_max_triples(n)
print(f"The maximum triples for {n} are: {max_triples}")
```

This will return the respective maximum triples for the given input.