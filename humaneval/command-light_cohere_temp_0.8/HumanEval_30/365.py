```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test case 1
def test1():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

#Test case 2
def test2():
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]

#Test case 3
def test3():
    assert len(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == 7 

#main function
if __name__ == "__main__":
    test1()
    test2()
    test3()
```
This Python script defines a function `get_positive` that takes a list as an argument and returns a new list containing only the positive numbers from the input list. The function uses list comprehension and a conditional statement to achieve this. The test cases, `test1`, `test2`, and `test3` are defined to verify the correctness of the `get_positive` function. The `test3` is a simple function that asserts that the `get_positive` function returns the correct list of positive numbers. The `main` function is responsible for running the tests and can be executed through the script using the Python `if __name__ == "__main__":` statement.