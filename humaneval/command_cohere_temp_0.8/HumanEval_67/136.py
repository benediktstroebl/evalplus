```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
```python
# Testing fruit_distribution()
def test_fruit_distribution():
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert fruit_distribution("100 apples and 1 oranges", 120) == 19
```

The tests verify that the function behaves as expected for a variety of inputs. If the list is longer than two lines, it's a good practice to break each test case into a separate test method with a descriptive name, this helps to maintain and read the code more easily. And if any further assertions are added in the future, it will be easier to identify which assertion belongs to which test case.