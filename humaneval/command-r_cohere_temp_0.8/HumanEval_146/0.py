```python
def specialFilter(nums):
"""Returns the number of elements in the array that are greater than 10 
and have odd first and last digits.
"""
    count = 0
    for num in nums:
        if num > 10:
            # Convert to string and get first and last digits
            num_str = str(num)
            if num_str[0] in '13579' and num_str[-1] in '13579':
                count += 1
    return count
```