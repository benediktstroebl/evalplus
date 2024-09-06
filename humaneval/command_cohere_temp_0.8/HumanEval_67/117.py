```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This problem can be solved by parsing the string input with the split(' and '), converting it to integers and subtracting them from the total number of fruits. Thus, the number of mangoes can be returned. 

Here are some test cases that can be used to validate the correctness of the approach:
```python
test_cases = [
    ("5 apples and 6 oranges", 19, 8),
    ("0 apples and 1 oranges", 3, 2),
    ("2 apples and 3 oranges", 100, 95),
    ("100 apples and 1 oranges", 120, 19),
    ("1 apples and 11 oranges", 33, 21),
    ("101 apples and 1 oranges", 120, 18),
    ("1 apples and 100 oranges", 120, 19),
    ("100 apples and 101 oranges", 220, 19)
]
``` 

With an input of test_cases, the above script should return the output expected per each test case.