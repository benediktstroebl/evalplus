```python
def triples_sum_to_zero(lst):
    if sum([x for x in lst if x <= 0]) == 0:
        return True
    return False

# Unit tests
tests = []

# Test 1
tests. generates list([1, 3, 5, 0])
tests.
# Test 2
tests += [[2, 4, -5, 3, 9, 7]]

# Test 3
tests += [[1])

# Run all tests to check the function correctness
if __name__ == "__main__":
    unittest.default_test.run_tests(triples_sum_to_zero, tests)
    print("All tests passed!")
```