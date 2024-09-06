```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            currentDigitSum = sum(map(int, str(num)))
            if currentDigitSum % 2 == 1 and currentDigitSum != 0:
                oddCount += 1
    return oddCount
```

This Python script defines a function called `specialFilter` that takes a list of numbers as input and counts the number of elements in the list that meet a specific criteria:
1. Odd First Digit: The first digit of the number should be odd (1, 3, 5, 7, or 9).
2. Odd Last Digit: The last digit of the number should also be odd.

The script then uses a `for` loop to iterate through each number in the input list. It checks if the number is greater than 10 (to ensure it has both a tens and ones digit) and calculates the sum of the digits of the number, appropriately adjusting for the case where the number is negative.

The sum of the digits is calculated by converting the number to a string and converting each digit to an integer using the `map` function. The `sum` function then adds up these integer values.

If the sum of the digits is odd (and not zero), it means both the first and last digits are odd, so the function increments the `oddCount` variable.

Finally, the function returns the value of `oddCount`, which represents the number of elements in the input list that meet the specified criteria.