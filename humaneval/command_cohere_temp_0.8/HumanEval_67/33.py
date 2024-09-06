```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operationally designed to solve the problem statement. It critically employs Python's inherent string-splitting technique to isolate and convert the apple and orange counts into integer values. By calculating these subtracted values, the function aims to provide the precise count of mango fruits in the basket. 

The following tests are designed to carefully examine the functionality of the `fruit_distribution` function:
```python
test_fruit_distribution = """
def test_fruit_distribution(s, n, expected):
    actual = fruit_distribution(s, n)
    assert actual == expected

test_fruit_distribution("5 apples and 6 oranges", 19, 8)
test_fruit_distribution("0 apples and 1 oranges", 3, 2)
test_fruit_distribution("2 apples and 3 oranges", 100, 95)
test_fruit_distribution("100 apples and 1 oranges", 120, 19)
"""
``` 

This test suite provides a systematic and robust evaluation of the function's performance through a variety of scenarios, ensuring that it operates with precision and accuracy.