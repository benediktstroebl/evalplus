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

The above function `specialFilter` goes through each number in the array and checks if it is greater than 10. For each such number, it converts it to a string and checks if the first and last digits are both odd. The total count of such numbers is then returned. 

You can test this function using various input arrays to ensure it behaves as expected. Feel free to add more test cases if needed.