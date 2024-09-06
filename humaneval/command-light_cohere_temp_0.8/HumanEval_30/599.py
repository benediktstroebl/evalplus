```python
def get_positive(input_list):
    return [num for num in input_list if num > 0]

# Test suite using nose2
test_suite = unittest.py(TestCase)(
    [
        ('get_positive', get_positive, [(-1, 2, -4, 5, 6))]),
        # Add more tests as needed
    ], 'test_get_positive.py')

```