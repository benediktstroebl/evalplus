```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
```python
# Test Suite
def test_fruit_distribution():
    # Case: Simple Example
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    # Case: Edge Case
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2
    # Case: Large Basket
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95
    # Case: Large Applies and Small Basket Size
    assert fruit_distribution("100 apples and 1 oranges", 120) == 19
```
This code defines a function `fruit_distribution` that takes two arguments: a string `s` and an integer `n`. The string `s` represents the number of apples and oranges in the basket, and the integer `n` represents the total number of fruits in the basket. 

The function extracts the number of apples and oranges from the string using `split(' and ')` and then converts these parts into integers. It then returns the number of mango fruits in the basket by subtracting the number of apples and oranges from the total number of fruits `n`.

The test suite includes four test cases that verify the function's behavior against various scenarios, ensuring that it correctly calculates the number of mango fruits as expected.