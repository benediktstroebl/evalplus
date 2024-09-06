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
The code defines a problem description, a solution in the form of a Python function, and a set of test cases to verify the correctness of the solution. 

The `fruit_distribution()` function takes two arguments: a string `s` and an integer `n`. This string `s` represents the number of apples and oranges in a basket of fruits. It splits the string into two integers representing the number of apples and oranges, respectively, and calculates the number of mangoes by subtracting the sum of apples and oranges from the total number of fruits. The result is the number of mangoes in the basket. 

The `test_fruit_distribution()` function creates four different scenarios in the form of assertions. Each one tests a specific case of the function with the proper input and the expected output.  Each assertion checks whether the actual result matches the expected result. 
If all assertions pass, it indicates that the `fruit_distribution()` function provides the expected results for the given inputs.  This full suite of tests helps establish confidence in the correctness of the solution.  The use of a testing framework like `pytest` is recommended for more complex projects, providing additional features and organization of test cases.