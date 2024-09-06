```python
def triples_sum_to_zero(l: list):
    return any(sum(x) <= 0 for x in l)

# Unit tests
test_triples_sum_to_zero = unittest.TestCase("list(range(1, 10)))
test_result = triples_sum_to_zero(test_triples_sum_to_zero)
test_result.TestAssertions = unittest.makeAssertions(test_result is False)
```
The test function uses the `any()` function to check if there are three distinct elements in the list that sum to zero. The function returns `True` if the test is successful and `False` otherwise.  The time function can be imported into the main project and used to solve the problem.