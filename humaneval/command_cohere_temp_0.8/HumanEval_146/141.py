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

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and both the first and last digits of a number are odd (1, 3, 5, 7, 9). The function uses a for loop to iterate through each number in the `nums` array and checks if the number is greater than 10. If so, it extracts the first and last digit of that number using string slicing and then checks if these digits are odd. If both are odd, it increments the `oddCount` variable, which is used to keep track of the count of numbers that pass the given condition. The function returns the value of `oddCount` at the end.

Here is a markdown code block incorporating a unit test to validate the functionality of the function:
```python
# Test the specialFilter function
def test_specialFilter():
    # Expected output: 1
    assert specialFilter([15, -73, 14, -15]) == 1

    # Expected output: 2
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # Expected output: 0
    assert specialFilter([11, 2, 37, 55, 99]) == 0
    # Expected output: 1
    assert specialFilter([21, 43, 5, 77, 99]) == 1
    # Expected output: 0
    assert specialFilter([1, 3, 5, 7, 9]) == 0
```

This test validates scenarios involving correct application of the function's criteria and returns expected values of 1, 2, and 0 respectively for the given input arrays.