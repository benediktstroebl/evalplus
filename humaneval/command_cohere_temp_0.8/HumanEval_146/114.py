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

The function uses a `for` loop to iterate through each element in the input array and checks if the element is greater than 10. If true, it extracts the first and last digit of that number using string manipulation, and then checks if these digits are odd. If both are odd, it increments the `oddCount` variable, which is used to keep track of the count. Finally, the function returns `oddCount`. 

The expected outcome for the provided examples is:
1. `specialFilter([15, -73, 14, -15]) => 1`
2. `specialFilter([33, -2, -3, 45, 21, 109]) => 2`

The script is self-contained and does not rely on any external modules or dependencies, making it easy to use and distribute.