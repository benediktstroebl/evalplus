```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else x + 1))

# Test cases
test_sort_even = unittest.TestCase("sort_even")
test_sort_even.run_tests(test_sort_even)
 ``` 
The function takes a list `l` as input and returns a new list `l'`, where the elements at odd indices are kept unchanged, while the elements at even indices are equal to the values of the corresponding even indices of `l`, but are sorted. The `key` argument in the `sorted` function is used to specify the sorting key, which is a lambda function that checks if the index is even or odd. 
The `test_sort_even` function is created using the `unittest` module, which creates a test suite and runs the tests using the `run_tests` method.