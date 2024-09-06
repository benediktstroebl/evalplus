```python
def specialFilter(nums):
    oddCount = 0
    for num in nums:
        if num > 10:
            curr = int(str(num)[0])
            last = int(str(num)[-1])
            if curr % 2 == 1 and last % 2 == 1:
                oddCount += 1
    return oddCount
```

The given code defines a Python function `specialFilter` that solves the problem as described in the markdown code block. It counts the numbers that are greater than 10 and have odd first and last digits in the list of numbers and returns the count. 

To do this, it sets a counter `oddCount` to zero and then iterates through each number in the input `nums` array. For each number, it checks if the number is greater than 10. If so, it extracts the first digit of the number using string slicing `str(num)[0]` and converts it to an integer `curr`. Similarly, it extracts the last digit of the number using string slicing `str(num)[-1]` and converts it to an integer `last`. Finally, it checks if both the first and last digits are odd (1, 3, 5, 7, or 9) using the modulo operator `% 2 == 1` and increments the counter `oddCount` if they are. The function then returns the final count of such numbers. 

The code is self-contained and does not rely on any external modules or dependencies, making it portable and easy to use in any Python environment. 

To verify the correctness of the solution, you can create a test case for it. For example:
```python
test_cases = [
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    ([25, 28, 49, 54, 59, 66, 77, 94, 101, 108], 3)
]

for test in test_cases:
    nums, expected = test
    actual = specialFilter(nums)
    assert actual == expected, f"Input {nums} expected {expected} actual {actual}"
```

The code above will check the correctness of the `specialFilter` function against the test cases provided.  This way, you can be confident that the function behaves as expected.  It gives a comprehensive understanding of the problem and provides a fully functional Python solution alongside tests to ensure reliability.  This is a good practice for organizing code and ensuring correctness in programming tasks.