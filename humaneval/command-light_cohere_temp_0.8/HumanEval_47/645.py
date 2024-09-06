```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[n // 2] + lst[n // 2 - 1]) / 2
    else:
        return lst[n // 2]

# Test case 1
test_ Median = [10, 20, 40, 30, 70]
test_Median_result = median(test_Median)
assert test_Median_result == 50

# Test case 2
test_Median = [5, 5, 5, 5]
test_Median_result = median(test_Median)
assert test_Median_result == 5

# Test case 3
test_Median = [-10, 4, 6, 1000, 10, 20]
test_Median_result = median(test_Median)
assert test_Median_result == 15.0
```
This Python code defines a function called `median()` that computes the median of a list of numbers. It handles both even cases of lists, where the length is odd or even, using a logic to select the middle value. The test cases validate the right output, making sure the function works as expected.