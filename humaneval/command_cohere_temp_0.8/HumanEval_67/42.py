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

The tests assert the function fruit_distribution() with different input values to verify the output. You can use it as a baseline for the function and then compare it with your version of the code to make sure you both implement the same logic. Let me know if you have any issues with the solution or any other ideas regarding this problem! I am glad to assist you further!