```python
def is_simple_power(x, n):
    return x ** n == x

# Test case 1
test_suite = unittest.TestCase("is_simple_power", [(-1, False), (2, True), (8, True), (3, False), (5, False)])

# Run the tests
test_suite.run()
```