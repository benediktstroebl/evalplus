```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the total number of fruits in the basket as a parameter and calculates the number of apples, oranges, and mango fruits by splitting the given string. It then calculates the number of mango fruits by simply subtracting the number of apples and oranges from the total number of fruits.

Here is the simple unit test that can verify the functionality of the code:
```python
def test_fruit_distribution():
    # Arrange
    def fruit_distribution(s, n):
        apples, oranges = map(int, s.split(' and '))
        return n - apples - oranges
    
    # Act
    result = fruit_distribution("5 apples and 6 oranges", 19)
    result_2 = fruit_distribution("0 apples and 1 oranges", 3)
    result_3 = fruit_distribution("2 apples and 3 oranges", 100)
    result_4 = fruit_distribution("100 apples and 1 oranges", 120)
    
    # Assert
    assert result == 8
    assert result_2 == 2
    assert result_3 == 95
    assert result_4 == 19
```