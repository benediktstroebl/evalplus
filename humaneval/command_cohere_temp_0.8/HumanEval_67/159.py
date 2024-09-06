```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
```python
# TEST CASES
def test_fruit_distribution():
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert fruit_distribution("100 apples and 1 oranges", 120) == 19
```
This code defines a function `fruit_distribution` that solves the problem as stated in the prompt. It dynamically extracts the number of apples and oranges from the input string, and returns the number of mangoes based on the given total number of fruits. 

The code also includes test cases to validate the behavior of the `fruit_distribution` function. You can add more tests to cover a variety of scenarios and ensure the correctness of the solution.