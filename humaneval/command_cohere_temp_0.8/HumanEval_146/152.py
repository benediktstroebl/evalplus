```python
def specialFilter(nums):
    odd_digits = [x for x in nums if int(x) > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1]
    return len(odd_digits)
```

This function `specialFilter` takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and have odd first and last digits. To achieve this, it filters the list of numbers by using a list comprehension that checks the three mentioned conditions for each element, `int(x) > 10`, `int(str(x)[0]) % 2 == 1`, and `int(str(x)[-1]) % 2 == 1`. It then returns the length of the resulting list of numbers that meet these criteria. 

The tests passed with this function include checking the truth of the conditions for the input list `[15, -73, 14, -15]` resulting in 1, and the input list `[33, -2, -3, 45, 21, 109]` resulting in 2. Feel free to add more test cases to verify the function's correctness across multiple scenarios.