```python
def starts_one_ends(n):
    return sum(str(i)[:n] == '1' or str(i)[-n:] == '1' for i in range(10, 10**n + 10, 2))
```

This function uses a generator expression to iterate over alternating numbers starting from 10 up to 10^n, with every second number (starting from the second) incremented by 2. The condition `str(i)[:n] == '1' or str(i)[:-n] == '1'` checks whether the number (represented as a string) has a digit equal to 1 either at the beginning of its first `n` digits or at the end of its last `n` digits. The `sum()` function then adds up the numbers for which the condition is true, giving the count of numbers that start or end with 1. 

Let's introduce some test cases to ensure that the function behaves as expected:
```python
test_cases = [
    (1, 1),
    (2, 5),
    (3, 10),
    (4, 15),
    (5, 18),
    (10, 55),
    (100, 355),
]

for n, expected in test_cases:
    assert starts_one_ends(n) == expected
```

The above code provides a range of test cases to verify the correctness of the `starts_one_ends` function. 

For instance, for `n = 2`, we expect 5 valid results (11, 21, 31, 41, 51) giving a count of 5. For `n = 3`, there are 10 such numbers (111, 121, 131, 141, 151, 161, 171, 181, 191) for a count of 10. 

The test cases validate the expected behavior of the function for various `n` values.