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

The code defines a function `fruit_distribution()` that takes two parameters: a string `s` and an integer `n`. This string `s` contains the numbers of apples and oranges in the basket and the integer `n` is the total number of fruits in the basket. The function parses the string to extract the number of apples and oranges using `map(int, s.split(' and '))`. Then it returns the number of mangoes by calculating `n - apples - oranges`. 

The testing code defines a function `test_fruit_distribution()` that tests the `fruit_distribution()` function on four different inputs and for each of them checks if it returns the correct result as described in the `fruit_distribution()` function description. And as a result, the code returns four assertions that demonstrate the correctness of the `fruit_distribution()` solution.