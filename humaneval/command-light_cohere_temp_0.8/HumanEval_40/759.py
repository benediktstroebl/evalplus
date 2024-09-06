```python
def triples_sum_to_zero(lst):
    return any(sum(a) == 0 for a in lst if len(set(a)) == 3)

# Unit tests
test_triples_sum_to_zero = [
    "def test_sum():
        assert triples_sum_to_zero([1, 3, 5])
        assert not triples_sum_to_zero([1, 2, 3])
        assert not triples_sum_to_zero([2, 4, -5])
        assert not triples_sum_to_zero([1,])
    ]

# Run the function and tests
triples_sum_to_zero(test_sum())
```