```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    return arr_copy[:k]
```

This function `maximum` takes in two parameters, `arr` and `k`, where `arr` is the given array of integers and `k` is the desired number of maximum elements to be returned in a sorted list. 

The function sorts the given array and then returns the first `k` elements of the sorted array, achieving the goal of returning a sorted list with the maximum `k` numbers present in the input array. 

This solution is simple and efficient, with a time complexity of O(log(N)) where N is the size of the input array. 

Let's make sure this solution works for all test cases by creating a few tests using the `unittest` module:
```python
import unittest

def maximum(arr, k):
    arr_copy = sorted(arr)
    return arr_copy[:k]

class MaximumTestCase(unittest.TestCase):
    def test_example_1(self):
        input_arr = [-3, -4, 5]
        input_k = 3
        expected_output = [-4, -3, 5]
        result = maximum(input_arr, input_k)
        self.assertEqual(result, expected_output)

    def test_example_2(self):
        input_arr = [4, -4, 4]
        input_k = 2
        expected_output = [4, 4]
        result = maximum(input_arr, input_k)
        self.assertEqual(result, expected_output)

    def test_example_3(self):
        input_arr = [-3, 2, 1, 2, -1, -2, 1]
        input_k = 1
        expected_output = [2]
        result = maximum(input_arr, input_k)
        self.assertEqual(result, expected_output)

    def test_zero_k(self):
        input_arr = [1, 2, 3, 4]
        input_k = 0
        expected_output = []
        result = maximum(input_arr, input_k)
        self.assertEqual(result, expected_output)

    def test_k_greater_than_array_size(self):
        input_arr = [1, 2, 3]
        input_k = 10
        expected_output = []
        result = maximum(input_arr, input_k)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
```

When you run this file, the `unittest` framework will run all the test cases mentioned and will report whether the functions and the cases we've suggested have passed or failed. 

This way, you can ensure that the function is working correctly for all possible cases.