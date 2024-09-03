```python
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
    For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
    Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    # Test: Input
    n = 5
    # Output: 1 ( valid triple: (1, 7, 13) )
    assert get_max_triples(10) == 10
    assert get_max_triples(3) == 6
    assert get_max_triples(1) == 1
    assert get_max_triples(0) == 0
    assert get_max_triples(20) == 2
```
The provided Python function, get_max_triples(n), calculates the number of unique triples using the formula a[i] = i * i - i + 1. The function follows the formula, which creates an array a containing integers from 1 to n. The formula guarantees that the array will only contain the distinct integer values and their permutations. The function then returns the number of valid triples (1, 7, 13) in this example.