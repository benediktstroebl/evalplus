```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the input string and integer to compute the number of mangoes with the given constraints.

To test this function, one can create a test case like this:
```python
test_cases = {
    ('5 apples and 6 oranges', 19): 8,
    ('0 apples and 1 oranges', 3): 2,
    ('2 apples and 3 oranges', 100): 95,
    ('100 apples and 1 oranges', 120): 19,
}

for string, num in test_cases.items():
    assert fruit_distribution(string, num) == test_cases[string]
```