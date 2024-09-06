```python
def triples_sum_to_zero(lst):
    # Write your code here
    seen = set()
    for a in lst:
        for b in lst:
            if a != b and sum([a, b, c]) == 0 and (a, b) not in seen:
                seen.add((a, b))
                if len(seen) == 3:
                    return True
    return False
```

The function `triples_sum_to_zero` works by checking every possible pair out of the given list `lst`. It initializes a set `seen` to track the seen combinations to avoid duplicates due to the unlimited pair checking loop. It returns True if the summation of three distinct elements in the list is zero, and False otherwise.

Here is a simpler approach that solves the problem:
```python
def triples_sum_to_zero(lst):
    return len(set(tuple(x) for x in zip(lst, lst[1:], lst[2:] ) if sum(x) == 0)) > 2
```
This approach works by using `zip` to pair the list with itself, dropping the first element and picking the second, then pairing that with the rest of the list, and summing these triples. If the sum is zero, it returns a set of tuples. Counting the number of unique tuples that sum to zero gives us the number of qualifying triplets out of the given list, and thus if this count is more than 2, it returns True.