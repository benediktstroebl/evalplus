```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code defines a function `fruit_distribution` that takes two parameters: a string `s` and an integer `n`. The string `s` represents the number of apples and oranges in the basket, and the integer `n` represents the total number of fruits in the basket.

The solution splits the string into an array of apples and oranges using the `split` method and then converts these array elements from strings to integers using the `map` method. It then returns the number of mangoes by subtracting the number of apples and oranges from the total number of fruits in the basket `n`.

Here is a test suite to check if the code is correct:
```python
def test_fruit_distribution():
    # Basic Test Cases
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Test Cases with Only Apples
    assert fruit_distribution("123 apples", 245) == 122

    # Test Cases with Only Oranges
    assert fruit_distribution("34 oranges", 252) == 228

    # Test Cases with Large Numbers
    assert fruit_distribution("1000 apples and 1001 oranges", 2001) == 1000

test_fruit_distribution()
``` 
The test suite includes basic, edge, and large-number cases to validate the `fruit_distribution` function.