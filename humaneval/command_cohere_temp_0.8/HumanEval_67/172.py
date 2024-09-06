```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This problem can be solved by splitting the input string into two integers that represent the number of apples and oranges. The function then returns the total number of fruits in the basket minus the number of apples and oranges. A test case is added to ensure that the function behaves correctly.

```python
test_case = """
    fruit_distribution("5 apples and 6 oranges", 19) -> 19 - 5 - 6 = 8
    """
assert fruit_distribution("5 apples and 6 oranges", 19) == 8
```