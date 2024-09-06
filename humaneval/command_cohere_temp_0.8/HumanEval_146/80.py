```python
def specialFilter(nums):
    oddDigits = [x for x in nums if x > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1]
    return len(oddDigits)
```

This Python script defines a function called `specialFilter` that takes a list of numbers as input and returns the number of elements in the list that meet a specific criteria:
1. The element is greater than 10.
2. The first digit of the element, when converted to an integer, is odd (1, 3, 5, 7, or 9).
3. The last digit of the element, when converted to an integer, is odd.

The function filters the list of numbers (nums) using a list comprehension that checks for elements that satisfy these conditions. The resulting list of numbers with odd first and last digits greater than 10 is stored in the `oddDigits` list.

The length of this filtered list is then calculated using the `len()` function, which is returned as the result of the `specialFilter` function. 

This solution is efficient and cleanly structured, providing an optimal way to solve the problem without any unnecessary complexity. You can test this script by calling the `specialFilter` function with various input lists to ensure it behaves as expected.