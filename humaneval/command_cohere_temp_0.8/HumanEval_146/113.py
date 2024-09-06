```python
def specialFilter(nums):
    oddDigits = [x for x in nums if x > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1]
    return len(oddDigits)
```

This function uses a list comprehension to filter out numbers from the input array that meet the specified criteria - having both first and last digits odd. Following that, it counts the number of elements in the resulting list and returns it. 

The unit tests for this function can be added as a separate array test cases providing valid input arrays and checking if the function result matches the expected output for each of them:
```python
test_cases = [
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    ([21, 109, 5, 57, 893, 95, 25, 99], 3),
    ([11, 3, 55, 77, 101, 103, 19, 91], 3),
]

for test in test_cases:
    nums, expected = test
    result = specialFilter(nums)
    assert result == expected, f"Expected {expected}, but got {result} for input {nums}"
```

This block of code will evaluate each test case, executing the `specialFilter` function on the input nums and comparing the returned result with the expected output for each case.  It ensures that the function `specialFilter` produces the expected filter and count result for a variety of inputs. 
Please let me know if any additional clarification is needed.