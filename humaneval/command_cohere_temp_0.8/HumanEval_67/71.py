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
The code defines a function `fruit_distribution` that takes two parameters: a string `s` and an integer `n`. This string `s` contains the count of apples and oranges in the basket, and the integer `n` represents the total count of fruits in the basket. 

The function extracts the counts of apples and oranges from the string using `split(' and ')` and then returns the count of mangoes by calculating `n - apples - oranges`. 

The code includes test cases to validate the behavior of the `fruit_distribution` function against four different scenarios.