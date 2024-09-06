```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list and then uses the sum function to add these numbers. 

Here is a test case that verifies the correct operation of the function:
```python
def test_add():
    # Arrange
    lst = [4, 2, 6, 7]

    # Act
    result = add(lst)

    # Assert
    assert result == 2, "Failed to add correct even elements at odd indices."
```
This test case verifies that the function correctly identifies and adds the even elements at odd indices from the input list. 

Thus, the function adheres to the problem description. 
If you have any more queries, please let me know!