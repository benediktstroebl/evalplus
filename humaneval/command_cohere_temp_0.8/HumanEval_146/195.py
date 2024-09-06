```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The Python script employs a nested list comprehension to identify numbers that meet the problem criteria. The outer comprehension `oddFirsts` filters numbers where the first digit is odd; `oddLasts` does the same for the last digit. The function then measures the intersection of the two lists, returning the count of numbers that satisfy both conditions. 

The solution adheres to Python's efficiency guidelines, completing within linear time complexity `O(n)` and linear space complexity `O(1)`.

This code may be tested against a variety of input number arrays to validate its correctness. Test cases might include:
```python
# Test case 1
nums = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
expected = 2
result = specialFilter(nums)
print(f"Test case 1: Expected {expected}, Actual {result}")

# Test case 2
nums = [15, 50, 23, 9, 64, 31]
expected = 3
result = specialFilter(nums)
print(f"Test case 2: Expected {expected}, Actual {result}")

# Test case 3
nums = [11, 3, 27, 99, 22, 57, 31]
expected = 3
result = specialFilter(nums)
print(f"Test case 3: Expected {expected}, Actual {result}")
```

This will help ensure the `specialFilter` function operates as expected across various scenarios.