```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            firstDigit = int(str(num)[0])
            lastDigit = int(str(num)[-1])
            if firstDigit % 2 == 1 and lastDigit % 2 == 1:
                oddCount += 1
    return oddCount
```

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and have odd first and last digits. It iterates through each number in the `nums` array and checks if the number is greater than 10. If so, it extracts the first and last digits of that number using string manipulation and ensures they are odd. If both digits are odd, it increments the `oddCount` variable, total count of such numbers. Finally, the function returns the `oddCount` variable. 

The test cases provided in the problem, along with additional test cases cover a variety of scenarios:
```python
def test_specialFilter():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([27, 51, 19, -137, 441, 0]) == 3
    assert specialFilter([111, 11, 333, 3, 555, 5]) == 3
    assert specialFilter([4, 5, 6, 7, 8, 9]) == 0
    assert specialFilter([12, 13, 14, 15, 16, 17]) == 0
    assert specialFilter([2, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 3
```