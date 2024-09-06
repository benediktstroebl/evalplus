```python
def triples_sum_to_zero(l: list):
    return sum([x for x in l if x in set([x for x in l]) <= 0]) == 0

# Test the function
l = [1, 3, 5, 0]
result = triples_sum_to_zero(l)
assert result == False, "Function failed the test"

l = [1, 3, -2, 1]
result = triples_sum_to_zero(l)
assert result == True, "Function failed the test"

l = [1, 2, 3, 7]
result = triples_sum_to_zero(l)
assert result == False, "Function failed the test"

l = [2, 4, -5, 3, 9, 7]
result = triples_sum_to_zero(l)
assert result == True, "Function failed the test"

l = []
result = triples_sum_to_zero(l)
assert result == False, "Function failed the test"
```