```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the two integers representing the number of apples and oranges from the **input string** and returns the number of mangoes by subtracting both numbers from the total number of fruits.

Here is the main part of the code where the program executes the function with test cases:
```python
test_cases = [("5 apples and 6 oranges", 19), ("0 apples and 1 oranges", 3), ("2 apples and 3 oranges", 100), ("100 apples and 1 oranges", 120)]

for string, n in test_cases:
    assert fruit_distribution(string, n) == 8, "Failed test 1"
```