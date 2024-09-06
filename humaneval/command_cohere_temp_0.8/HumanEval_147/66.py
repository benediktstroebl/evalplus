```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate max triples
    triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j] + a[j-i-1]) % 3 == 0:
                triples += 1
    return triples
```
This script creates the sequence of numbers as described in the prompt and then iterates through all possible pairs of elements in the sequence, checking whether the sum of the differences of the two elements is divisible by three. The script then returns the number of valid triplets, as described in the prompt.

To get the actual maximum number of triples, you would need to multiply the return value by 2, as it is the maximum possible, and for a maximum configuration, you would have two choices for each element (whether to include it in a triplet or not).