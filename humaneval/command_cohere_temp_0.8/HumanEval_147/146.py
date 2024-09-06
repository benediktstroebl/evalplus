```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum triples
    triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            curr = a[i] + a[j]
            if curr % 3 == 0:
                triples += 1
    return triples
```
This Python script defines the 'get_max_triples' function, which takes a positive integer 'n' as input and returns the number of triples from the sequence 'a' that satisfy the problem's criteria. It creates the sequence 'a' as specified in the prompt and then iterates through all possible pairs of elements from the sequence. If the sum of two elements is divisible by 3, it counts a triple, as indicated by the 'triples' variable. Ultimately, it returns the total count of qualifying triples.