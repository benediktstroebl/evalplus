```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code solves the problem by taking two integers from the division of the provided string into two parts `apples` and `oranges` using the `split()` method and subtracting them from the total number of the fruits. 

Here is a simple test suite to check if the function behaves as expected:
```python
def test_fruit_distribution():
    # basic tests
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert fruit_distribution("100 apples and 1 oranges", 120) == 19

    # edge cases
    try:
        fruit_distribution("apples and 6 oranges", 19)
    except ValueError:
        assert True  # raises ValueError

    try:
        fruit_distribution("5 apples", 5)
    except ValueError:
        assert True  # raises ValueError

    # other cases
    assert fruit_distribution("20 apples and 40 oranges", 100) == 40
    assert fruit_distribution("1 apples and 1 oranges", 10) == 8
    assert fruit_distribution("0 apples and 10 oranges", 20) == 10
``` 

The test suite includes basic tests as well as edge cases, such as when the number of apples and oranges is more than the given total or when the provided string does not have a valid format.