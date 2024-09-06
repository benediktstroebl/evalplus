```python
def specialFilter(nums):
    oddFirsts = [num for num in nums if int(num[0]) % 2 == 1]
    oddLasts = [num for num in nums if int(num[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script employs a logical operator ('&') to filter numbers that satisfy conditions of both odd first and last digits to eliminate any duplicates and then uses `len()` to count the number of elements in this filtered array. The function returns this count. This solution is efficient and uses both inpatient and outpatient filtering. The inpatient filtering is done to find odd last digits and the result is used for filtering odd first digits, which is an outpatient filtering. 
Output: