```python
def double_the_difference(nums):
    odd_squares = [x ** 2 for x in nums if x % 2 == 1 and x >= 0]
    return sum(odd_squares) if odd_squares else 0
```

The function `double_the_difference` uses a list comprehension to filter the `nums` input list and create an `odd_squares` list containing the squares of numbers that are odd and non-negative. Then, it returns the sum of squares if the `odd_squares` list is not empty, or 0 if it is empty. This is done to handle the scenario of an empty list also, as per the test case provided. 

This approach ensures the functionality works as per the given test cases.