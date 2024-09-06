```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            curr = str(num)
            if curr[0] in ('1', '3', '5', '7', '9') and curr[-1] in ('1', '3', '5', '7', '9'):
                oddCount += 1
    return oddCount
```

The algorithm behind the script is fairly simple. The function `specialFilter` operates on a list of numbers, `nums`. It first establishes a counter, `oddCount`, to tally the number of numbers that fit the criteria. The function then iterates through each number in the list using a `for` loop. For each number, it first assesses whether the number is greater than 10. If so, it transforms the number into a string using `str(num)`. Next, it evaluates whether the first digit of the string is odd and simultaneously checks if the last digit is also odd. If both conditions are true, the count is incremented by 1. Finally, the function returns the value of `oddCount` to convey the total count of numbers that conform to the specified criteria. 

To ensure that the function is well-tested, it would be beneficial to establish test cases that cover a gamut of scenarios. Here are some recommendations for test cases that could be integrated into a single script under a `test_specialFilter` function:
1. **Basic Test Case**: This test case establishes the fundamental correctness of the function. It should encompass an array of numbers that includes both numbers that meet the specified criteria and those that don't. 

Example:
```python
def test_specialFilter(nums_list):
    # Sample array of numbers
    nums = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
    
    # Expected count derived from the sample array
    expected = 1
    
    # Test the function
    result = specialFilter(nums)
    assert result == expected
```
2. **Edge Cases**: These test cases scrutinize how the function behaves when presented with lists that include minimal or no numbers that meet the specified criteria. 

Example:
```python
def test_specialFilter_edge_cases(nums_list):
    # List with only numbers that satisfy the criteria
    nums = [15, 51, 35, 37, 53]
    
    # List with only numbers that do not satisfy the criteria
    nums = [2, 4, 20, 0, 100]
    
    # List with a mix of numbers, some satisfying and some not
    nums = [15, 34, 27, 26, 105, 33, 9, 19, 302]
    
    # Expected counts for each case
    expecteds = [3, 0, 2, 1]
    
    for i in range(len(nums)):
        result = specialFilter(nums[i])
        assert result == expecteds[i]
```
3. **Large List**: This test case validates the function's performance on a list of numbers with a substantial size. This is crucial to assess the function's efficiency. 

Example:
```python
def test_specialFilter_large_list(nums_list):
    # Generating a list of 1000 numbers, half of which satisfy the criteria
    nums = [(i+1) if i % 2 == 0 else (i+3) for i in range(1000)]
    
    expected = int(len(nums) / 2)
    
    # Testing the function
    result = specialFilter(nums)
    assert result == expected
``` 
By