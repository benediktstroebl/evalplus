```python
def specialFilter(nums):
    oddDigits = [x for x in nums if x > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1]
    return len(oddDigits)
```

This Python script defines a function called `specialFilter` that takes a list of numbers as input and returns the number of elements in the list that meet a specific criteria:
1. `x > 10`: The element is greater than 10.
2. `int(str(x)[0]) % 2 == 1`: The first digit of the element is odd.
3. `int(str(x)[-1]) % 1 == 1`: The last digit of the element is odd.

The function filters the list based on these conditions and returns the count of numbers that fulfill all three criteria. The overall complexity is O(n), where n is the length of the input list `nums`.  This is because it iterates through each element once, performing operations that are O(1) each: checking inequalities, extracting characters, and checking for odd digits.