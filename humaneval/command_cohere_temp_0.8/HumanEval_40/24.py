```python
def triples_sum_to_zero(lst):
    # Split the list into chunks of three to efficiently check for triples
    # that sum up to zero.
    triples = [(lst[i:i+3]) for i in range(0, len(lst), 3)]
    
    # Iterate through the chunks and return True if a valid triple is found.
    for triple in triples:
        if sum(triple) == 0:
            return True
    
    return False
```

This approach divides the list into groups of three elements (using chunking) and then checks if any of those groups sum up to zero. This allows for an efficient checking process without the need to iterate through the list multiple times.