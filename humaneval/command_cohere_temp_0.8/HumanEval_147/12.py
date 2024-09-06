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

The script creates the array `a` as specified in the prompt. It then iterates through the array and calculates the valid triples, counting them using the `triples` variable. 

To ensure the accuracy of the solution, we recommend adding appropriate tests to validate the code. 
These tests can include different `n` values and validate the correctness of the output. 

You can use tools such as `unittest` or `pytest` to create test suites and assert the expected results against the actual outputs.