```python
def specialFilter(nums):
    return len([x for x in nums if (x > 10) and (x[0] == int(x[0]) & 1) and (x[len(x) - 1] == int(x[len(x) - 1]) & 1))

# Test the function with a few examples
test_nums = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
res = specialFilter(test_nums)
print("Result:", res)

# Test again with input validation error (to trigger TypeError)
test_nums = [15, -73, 14, -15]
try:
    specialFilter(test_nums)
except TypeError:
    print("Error:", "Input must be a list.")
```