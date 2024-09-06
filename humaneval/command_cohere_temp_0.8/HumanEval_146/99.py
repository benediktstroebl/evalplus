```python
def specialFilter(nums):
    oddFirst = [x for x in nums if int(x[0]) % 2 == 1 and int(x[1]) % 2 == 1 and x > 10]
    return len(oddFirst)
```

The provided Python script defines a function called `specialFilter` that takes a list of numbers as input. It filters this list to include only those elements that are greater than 10 and have both the first and last digits odd (1, 3, 5, 7, or 9). The function then returns the count of such numbers present in the list.

To achieve this, it employs a list comprehension, which helps filter and iterate over the list efficiently. For each number in the input list, it checks two things:
1. `int(x[0]) % 2 == 1`: This verifies if the number's first digit, when converted to an integer and modulo-divided by 2, yields a remainder of 1. This implies that the first digit is odd.
2. `int(x[1]) % 2 == 1`: Similarly, it checks if the number's last digit is also odd. Here, `x[1]` is used to refer to the second character of the string, which effectively targets the last digit.

Lastly, the length of this filtered list is returned, indicating the count of numbers in the input that satisfy the defined criteria. The script returns the count of numbers that are greater than 10 and have both first and last digits odd.