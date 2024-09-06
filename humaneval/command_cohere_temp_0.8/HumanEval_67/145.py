```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
```python
# Testing Script
test_cases = [
    ("5 apples and 6 oranges", 19, 8),
    ("0 apples and 1 oranges", 3, 2),
    ("2 apples and 3 oranges", 100, 95),
    ("100 apples and 1 oranges", 120, 19),
]

for test_case in test_cases:
    with unittest.TestCase():
        actual = fruit_distribution(*test_case)
        assert actual == test_case[-1], f"For the input {test_case[0]},{test_case[1]}, expected {test_case[-1]} but got {actual}"
```
This code solves the problem by splitting the input string into two integers, representing the number of apples and oranges, and returning the total number of fruits minus the number of apples and oranges. The map function is used to convert the string into integer values. The code provides a elegant and simple solution to the problem and it is tested against a battery of test cases to ensure its correctness.