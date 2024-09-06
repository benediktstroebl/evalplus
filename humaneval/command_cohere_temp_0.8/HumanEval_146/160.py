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

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and have odd first and last digits. It loops through each number in the `nums` array, checks if it's greater than 10, and then checks if the first and last digits of its decimal representation are odd. The total count of such numbers is then returned. 

The unit test for this function (not included in the above markdown code block) could be defined as:
```python
def test_special_filter():
    # Example cases from the problem statement
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Added test cases for comprehensive coverage
    assert specialFilter([11, 21, 41, 43, 51]) == 4
    assert specialFilter([31, 13, 47, 53, 59]) == 5
    assert specialFilter([1, 3, 5, 7, 9]) == 0 
    assert specialFilter([11, 13, 17, 19, 21]) == 0 
    assert specialFilter([21, 23, 25, 27, 29]) == 1 
    assert specialFilter([31, 33, 35, 37, 39]) == 2 
    assert specialFilter([41, 43, 45, 47, 49]) == 3 
    assert specialFilter([51, 53, 55, 57, 59]) == 4 
    assert specialFilter([61, 63, 65, 67, 69]) == 5 
    assert specialFilter([71, 73, 75, 77, 79]) == 6 
```

This test suite covers multiple scenarios to ensure the `specialFilter` function behaves as expected.