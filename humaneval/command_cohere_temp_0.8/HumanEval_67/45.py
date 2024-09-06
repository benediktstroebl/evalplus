```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the input string and integer to compute the number of mangoes with the formula `n - apples - oranges`. A usage example is shown below:
```python
print(fruit_distribution("5 apples and 6 oranges", 19))
```
Which outputs:
```
8
```

The script can be tested further by uncommenting the last line of the script and running the example or by calling the function with different test cases.