Here's a Python script that includes a function to solve the given problem and a separate test module:
```python
# solution.py
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum

# tests.py
def test_min_subarray_sum():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([1, -1, 1, -1, 1]) == 0
    assert minSubArraySum([0, 0, 0, 0]) == 0
    assert minSubArraySum([0, 0, 0, 0, 0, 0]) == 0
    assert minSubArraySum([2, -1, 1, -5, 2, 0, -2]) == -1

# Run the tests
test_min_subarray_sum()
```
The `minSubArraySum` function uses dynamic programming to compute both the minimum and maximum sum potentials of each element in the array. This approach allows us to efficiently calculate the minimum sum of any non-empty sub-array. The `test_min_subarray_sum` function provides example use cases to verify the correctness of the solution.

To run the tests, simply call `test_min_subarray_sum()`. The detailed explanation of the dynamic programming approach is as follows:
The dynamic programming approach to finding the minimum sum of a sub-array is to consider both the current element and the sum of the previous element. This way, you have an optimal sub-array if you take the minimum of these two values for each element in the array.

Here's the step-by-step breakdown:
1. `min_sum` and `max_sum` are initialized with the first element of the array `nums[0]`.
2. For each subsequent element `n` in the array, update `min_sum` and `max_sum` as follows:
   - `min_sum` is updated by taking the minimum of `n` and `min_sum + n`. The idea is to keep track of the smallest sum of any sub-array ending at the current element `n`.
   - `max_sum` is updated by taking the maximum of `n` and `max_sum + n`. The idea is to keep track of the largest sum of any sub-array ending at the current element `n`.
3. After processing all elements, the `minSubArraySum` returns the sum of `min_sum` and `max_sum`. This is because the answer is the smallest sum of any sub-array ( Guaranteeed by keeping track of `min_sum` ) plus the largest sum of any sub-array ( Guaranteed by keeping track of `max_sum` ).

The approach guarantees finding the minimum sum of any non-empty sub-array in one pass with linear space complexity (since both `min_sum` and `max_sum` need extra storage).