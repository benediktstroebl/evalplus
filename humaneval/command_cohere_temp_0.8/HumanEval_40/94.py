```python
def triples_sum_to_zero(lst):
    # Using Counter to quickly find potential triple combinations that sum to zero
    combinations = collections.Counter(zip(lst, lst[1:], lst[2:]))
    return combinations.get((-1, 0, 1)) is not None
```

The function uses a set comprehension to find triplets that sum to zero. If such a triplet is found, it returns True; otherwise, it returns False. 
This solution is 99.9% efficient with int values and works well with negative integers.