```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currentDigit1 = int(str(num)[0])
            currentDigit2 = int(str(num)[-1])
            if currentDigit1 % 2 == 1 and currentDigit2 % 2 == 1:
                oddCount += 1
    return oddCount
```

This script defines a function called `specialFilter` that takes in one parameter, an array of numbers, and correctly solves the problem as described in the markdown code block. It loops through each number in the `nums` array, checks if it is greater than 10, and then checks whether the first and last digits of the number are odd. It returns the number of elements that are both greater than 10 and have odd first and last digits. 

The script passes the test cases provided in the description, such as `specialFilter([15, -73, 14, -15]) => 1` and `specialFilter([33, -2, -3, 45, 21, 109]) => 2`. 
It is also scalable and will produce correct results for any other provided test cases as long as they are formatted correctly.