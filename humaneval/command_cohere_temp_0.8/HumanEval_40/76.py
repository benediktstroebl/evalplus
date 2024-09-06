```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    l2 = l[:]
    l2.sort()
    for i in range(len(l2) - 2):
        for j in range(i + 1, len(l2) - 1):
            if l2[i] + l2[j] + l2[j + 1] == 0:
                return True
    return False
```

Here's a usage example:
```python
result = triples_sum_to_zero([1, 3, 5, 0])
print(result)  # Output: False
```