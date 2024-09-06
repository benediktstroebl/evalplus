Here's a Python script that contains a function eat() that solves the problem described in the code block above:
```python
def eat(n, need, rem):
    ate = n + min(need, rem)
    rem = max(0, rem - need)
    return [ate, rem]

# Tests
test_cases = [
    [5, 6, 10, 11, 4],
    [4, 8, 9, 12, 1],
    [1, 10, 10, 11, 0],
    [2, 11, 5, 7, 0]
]

for case in test_cases:
    assert eat(*case) == case[-1:]
```
This code includes a list of test_cases, each of which consists of the input parameters n, need, rem, and the expected output [ate, rem]. The function eat() is called in each test case and the returned value is compared to the expected output using the assert statement.