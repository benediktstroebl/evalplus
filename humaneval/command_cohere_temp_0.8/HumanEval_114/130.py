Here's a Python script that includes a function to solve the given problem and a separate function to handle testing:
```python
def minSubArraySum(nums):
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    
    for num in nums[1:]:
        min_sum = min(num, min_sum + num)
        max_sum = max(max_sum, num)
    
    return min_sum + max_sum if max_sum else min_sum

def test_min_sub_array_sum():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([0, 0, 0, 0]) == 0

test_min_sub_array_sum()
```

The function `minSubArraySum` works by initially considering the first element of the array as both the potential minimum and maximum sum. It then iterates through the rest of the array, updating these two values accordingly. Finally, the function returns the sum of the minimum and maximum values, but if there's no maximum (i.e., the array contains all negative numbers), it returns just the minimum sum. 

The `test_min_sub_array_sum` function is provided to demonstrate how to verify the functionality of the `minSubArraySum` function. In this case, it simply asserts the correct behavior for two different scenarios. You can add more tests as needed.