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

This function `specialFilter` takes an array of numbers (`nums`) as input and counts the number of elements in the array that meet the following criteria:
1. They must be greater than 10. 
2. The first and last digits of the number should be odd (1, 3, 5, 7, or 9). 

The function uses a `for` loop to iterate through each element in the `nums` array and checks if the element is greater than 10. If true, it extracts the first and last digit of the number using string manipulation, and then checks if both these digits are odd. If the condition is satisfied, the count `oddCount` is incremented. Finally, the function returns the `oddCount` variable. 

The expected output for the given examples is:
1. `specialFilter([15, -73, 14, -15]) => 1`
2. `specialFilter([33, -2, -3, 45, 21, 109]) => 2`

The script passes the tests if the context entails testing the code against some example data. 

ukasz-malucha
```python
def test_specialFilter():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([27, 51, 59, 93]) == 3
    assert specialFilter([11, 19, 31, 43, 51]) == 0
    assert specialFilter([17, 97, 71, 99, 23]) == 1
```