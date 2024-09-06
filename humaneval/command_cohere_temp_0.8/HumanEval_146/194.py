```python
def specialFilter(nums):
    oddDigits = [x for x in nums if x > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1]
    return len(oddDigits)
```

This Python script defines a function called `specialFilter` that takes a list of numbers as input and returns the number of elements in the list that meet a specific criteria:
1. `x > 10`: The element is greater than 10.
2. `int(str(x)[0]) % 2 == 1`: The first digit of the element is odd.
3. `int(str(x)[-1]) % 2 == 1`: The last digit of the element is odd.

The list comprehension `oddDigits` creates a list of all the elements in `nums` that satisfy all these conditions. The function then returns the length of this `oddDigits` list, which is the number of elements in the input list that meet the specified criteria.

Here is a more detailed explanation of the code:
- The `oddDigits` list comprehension uses a nested condition: `x > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1` to filter the list of numbers.
- The first condition `x > 10` ensures that only numbers greater than 10 are considered.
- The next two conditions check if the first and last digits of a number are odd (`1`, `3`, `5`, `7`, or `9`). The `int(str(x)[0])` converts the first digit to an integer to perform the check, and `int(str(x)[-1])` converts the last digit to an integer for the last digit check.
- The length of `oddDigits` is returned as the final result, which is the number of elements in the input list that satisfy all the conditions. 

This function will return the correct count of numbers that meet the specified criteria in the input list.