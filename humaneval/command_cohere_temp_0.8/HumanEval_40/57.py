```python
def triples_sum_to_zero(lst):
    # Write your code here. Read the markdown for more info on the problem.
    # Triple: (-2, 4, 6) sum to 0
    return any(sum(eltriple) == 0 for eltriple in itertools.combinations_with_replacement(lst, 3))
```

This code uses `any` and `itertools.combinations_with_replacement` to generate all triples from the list and check if their sum is equal to zero.

To understand how this code works, let's break it down step-by-step:
1. `any` is a built-in Python function that takes an iterable (in our case, a generator expression) and returns `True` if any element in that iterable is `True`. 

2. The generator expression in the any call is created using `itertools.combinations_with_replacement(lst, 3)`. This generates all possible triples from the input list using the `itertools` library. 

3. For each triple, the line `sum(eltriple) == 0` checks if the sum of the elements in the triple is equal to zero. 

4. If any of these triples sums to zero, the `any` function will return `True`. If none of the triples sum to zero, it will return `False`. 

This solution is efficient because it uses Python's built-in functions and libraries to handle the problem seamlessly.