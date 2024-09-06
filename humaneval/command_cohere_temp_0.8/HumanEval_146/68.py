```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currentDigitValue = int(str(num)[0])
            lastDigitValue = int(str(num)[-1])
            if currentDigitValue % 2 == 1 and lastDigitValue % 2 == 1:
                oddCount += 1
    return oddCount

# Test Cases
nums1 = [15, -73, 14, -15]
nums2 = [33, -2, -3, 45, 21, 109]
print(specialFilter(nums1))  # 1
print(specialFilter(nums2))  # 2
```

The function `specialFilter` goes through each number in the `nums` array. It checks if the number is greater than 10, and if so, it evaluates the first and last digits of that number by converting it to a string, extracting the first and last digits, and converting them back to integers. Using the modulus operator (`%`), it checks if both digits are odd (1, 3, 5, 7, or 9). If both digits are odd, it increments the `oddCount` variable, and finally, the function returns the `oddCount` value. The provided test cases succeed with the expected output. 

The solution is concise and efficient, providing a low time complexity of `O(n)` since it only iterates through the array once to verify the condition. In summary, the given code provides an accurate solution to the problem statement and fulfills the requirements. 
```