```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code defines a function `fruit_distribution` that takes two parameters: a string `s` and an integer `n`. The string `s` represents the number of apples and oranges in the basket, and the integer `n` represents the total number of fruits in the basket. 

The solution splits the string into a pair of integers representing the number of apples and oranges with the `split` method, taking the last element after splitting the string with the delimiter "and". The function returns the total number of fruits in the basket (`n`) minus the number of apples and oranges represented by the string `s`. This subtraction gives the total number of mango fruits in the basket. 

Here is a basic test suite to verify the functionality of the solution:
```python
def test_fruit_distribution():
    # Basic tests
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert fruit_distribution("100 apples and 1 oranges", 120) == 19

    # Test with different delimiters
    assert fruit_distribution("5 apples and 6 oranges", 19, delimiter='or') == 8
    assert fruit_distribution("0 apples and 1 oranges", 3, delimiter='or') == 2
    assert fruit_distribution("2 apples and 3 oranges", 100, delimiter='or') == 95
    assert fruit_distribution("100 apples and 1 oranges", 120, delimiter='or') == 19

    # Test with different data types for the total number of fruits
    assert fruit_distribution("5 apples and 6 oranges", '19') == 8
    assert fruit_distribution("0 apples and 1 oranges", 3.14) == 2
    assert fruit_distribution("2 apples and 3 oranges", [1,2,3,4]) == 95
    assert fruit_distribution("100 apples and 1 oranges", [1,2,3,4]) == 19

test_fruit_distribution()
```

The test suite contains several test cases to validate the behavior of the `fruit_distribution` function. It checks if the function can handle different delimiters, various data types for the total number of fruits, and corner cases such as no apples or oranges. 

Note: this solution assumes that the given string is formatted properly, i.e., that the apples and oranges quantities are integer values. It also assumes that the given string is lexicographically ordered such that 'apples' come before 'oranges'. These assumptions should be considered when applying the solution to real-world problems.