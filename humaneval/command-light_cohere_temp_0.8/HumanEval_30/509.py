```python
def get_positive(input_list):
    positive_numbers = [num for num in input_list if num >= 0]
    return positive_numbers

# Unit tests
test_get_positive = []
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_get_positive.push(get_positive(input_list))
input_list2 = [5, 3, -5, 2, -3, 3, -2, 3, 9, 0, -9]
test_get_positive.push(get_positive(input_list2))

def test_suite(test_func):
    test_func()
    test_list = [test_case() for test_case in test_cases]
    test_runner = unittest.runner.result()
   ard print("..." * 40)
    test_runner.start()
    partners = test_suite.master()
test_runner.now()
test_runner.result.assertEqual() is results a Brewer6 tests
```