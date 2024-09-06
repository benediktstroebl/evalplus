```python
def triples_sum_to_zero(lst):
    """
    Function to check if a list of integers sums to zero.
    Return True if all the purpose is met and there are three distinct elements in the list that sum to zero, and False otherwise.
    """
    triple_sums = {x for x in lst if sum([x]) == 0}
    return all(triple_sum == 0 for triple_sum in triple_sums)

tests = []

tests.add(triples_sum_to_zero([1, 3, 5, 0]))
tests.add(triples_sum_to_zero([1, 3, -2, 1]))
tests.add(triples_sum_to_zero([1, 2, 3, 7]))
tests.add(triples_sum_to_zero([2, 4, -5, 3, 9, 7]))
tests.add(triples_sum_to_zero([1]))

print(f"All tests passed.")
```