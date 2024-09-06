```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
```python
# Testing Script
test_cases = [
    ("5 apples and 6 oranges",19, 8),
    ("0 apples and 1 oranges",3, 2),
    ("2 apples and 3 oranges",100, 95),
    ("100 apples and 1 oranges",120, 19)
]

for test in test_cases:
    with assertEqual(test[2], fruit_distribution(*test)) as msg:
        print(msg)
```
Output:
```
assertEqual(2, 8, 'Generated Result is Incorrect')
assertEqual(3, 2, 'Generated Result is Incorrect')
assertEqual(95, 100, 'Generated Result is Incorrect')
assertEqual(19, 120, 'Generated Result is Incorrect')
```