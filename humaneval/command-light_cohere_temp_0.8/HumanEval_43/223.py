```python
def pairs_sum_to_zero(l):
    return any(x + y <= 0 for x, y in zip(l, l[1:]))

# Run tests
test_succ = unittest.TestCase("test_pairs_sum_to_zero", [1, 3, -2, 1], [False])
test_succ.addFailure(TestResultdoesNotEqual([1, 3, -2, 1]), 2)
test_succ.addFailure(TestResultDoesNotEqual([1, 2, 3, 7]), 2)
test_succ.addFailure(TestResultIsEqual([2, 4, -5, 3, 5, 7]), 0)

# Run suite
if __name__ == "__main__":
    unittest.run_unittest(test_succ)
 ``` 
The function `pairs_sum_to_zero` takes a list of integers as an argument. It returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. The function uses the `zip` to iterate over the list and checks if any element in the list plus the corresponding element in the list at the same index results in a non-negative number. 

The test function `test_pairs_sum_to_zero` tests the `pairs_sum_to_zero` function with a list of integers. It passes the test `test_succ` with a list of integers and a list of expected results. The test suite is run using the `unittest.run_unittest` function.