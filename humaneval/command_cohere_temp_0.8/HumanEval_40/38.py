```python
def triples_sum_to_zero(l: list):
    # Write your code here.
    seen = set()
    for a, b in itertools.combinations(l, 2):
        if a + b == 0 and (a, b) not in seen:
            seen.add((a, b))
            if len(seen) == 3:
                return True
    return False
```

The function uses a set called 'seen' to track the pairs (a, b) that have been seen so far. It iterates over all pairs of elements in the list, and for each pair, it checks whether their sum is zero. If it is, and this particular pair has not been seen before, it adds it to the 'seen' set. Once the set contains three different pairs, it returns True, indicating that there are three distinct elements in the list that sum up to zero. If the set isn't populated with three pairs within the loop, it returns False. 

This solution is efficient since it uses only one loop and takes advantage of set operations to track the distinct pairs efficiently.