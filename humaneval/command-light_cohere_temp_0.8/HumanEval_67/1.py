```python
def fruit_distribution(total_fruits,total_apples,total_oranges):
    return total_oranges - total_fruits - total_apples

#Test the function
def test_fruit_distribution():
    total_fruits = 5
    total_apples = 6
    total_oranges = 19
    result = fruit_distribution(total_fruits,total_apples,total_oranges)
    assert result == 8, "The result is not 8!"
    total_fruits = 0
    total_apples = 1
    total_oranges = 3
    result = fruit_distribution(total_fruits,total_apples,total_oranges)
    assert result == 2, "The result is not 2."
```

This code defines a function called fruit_distribution that takes in three parameters: total_fruits, total_apples, and total_oranges. The function then returns the the number of oranges in the basket. The function is then tested with a function called test_fruit_distribution that tests the function with different inputs.