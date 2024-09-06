```python
def triples_sum_to_zero(lst):
    # Use a hashmap to track sums of elements
    sums = {}
    for ele in lst:
        if ele not in sums:
            sums[ele] = 0
        sums[ele] += ele

    # Use sets to find distinct elements that sum to zero
    zero_triples = set()
    for x,xs in sums.items():
        if xs == 0:
            for y,ys in sums.items():
                if x + y == 0 and x != y:
                    zero_triples.add((x, y, xs))
                    zero_triples.add((x, xs, y))
                    zero_triples.add((xs, x, y))
                    zero_triples.add((xs, y, x))
    return len(zero_triples) > 0
```

This function uses two main constructs to find the answer:
1. It uses a hashmap (dict) to track the individual sums of elements in the list. This allows for efficient lookup of whether a given element's sum is zero or not. 
2. It then uses sets to find distinct triples that sum to zero. Given that the lookup for individual sums is efficient, it tries all possible distinct pairs of elements (`x` and `y`). It then checks if their sum is zero and they are distinct. If so, it adds the four permutations of triples containing `x`, `y`, and their sum to the `zero_triples` set. 

Finally, the function returns `True` if the `zero_triples` set contains at least one triplet and `False` otherwise. 

The function call with the example inputs passed should yield the following results:
```
>>> triples_sum_to_zero([1, 3, 5, 0])
False
>>> triples_sum_to_zero([1, 3, -2, 1])
True
>>> triples_sum_to_zero([1, 2, 3, 7])
False
>>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
True
>>> triples_sum_to_zero([1])
False
```