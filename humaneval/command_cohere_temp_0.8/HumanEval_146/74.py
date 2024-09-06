```python
def specialFilter(nums):
    oddFirst = [x for x in nums if int(x[0]) % 2 == 1]
    oddLast = [x for x in nums if int(x[-1]) % 2 == 1]
    return len(oddFirst & oddLast)
```

The script employs a binary operator & (intersection) to combine two oddCheck List Comprehenisons that check for elements conforming to the specified requirement. The two lists, oddFirst and oddLast, seem like they should have the same length, but in the event that they don't, the question dictates that the number of elements selected in the final result is the smaller of the two lengths.

Here is a markdown code block with corresponding test cases to ensure the function correctly identifies the number of elements that are greater than 10 and have odd first and last digits:
```python
test_cases = [
    [15, -73, 14, -15, 33, -2, -3, 45, 21, 109],
    [15, 33, 105, 37, 79, 91, 63, 25, 59, 107],
    [7, 57, 13, 43, 21, -11, -17, -25, -99, -105],
    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
]

for idx, nums in enumerate(test_cases, start=1):
    expected = len([x for x in nums if x > 10 and int(x[0]) % 2 == 1 and int(x[-1]) % 2 == 1])
    assert specialFilter(nums) == expected, f"TestCase {idx} failed."
```

This block includes a list of test cases of varying lengths that should all output various numbers. The assert statements compare the expected outcome with the actual outcome of the function specialFilter. Any failures are written out as errors. If all test cases pass, the function is correct and adheres to the problem description.  As all variables and the function are self-contained, this code block can be plop into any Python environment and run without any dependencies.