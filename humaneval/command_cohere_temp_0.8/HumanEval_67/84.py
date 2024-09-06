```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the two integers representing the number of apples and oranges from the string using `map()` along with the total number of fruits in the basket. It then finds the number of mangoes by subtracting both apples and oranges from the total number of fruits.

Here's an example usage of the function:
```python
print(fruit_distribution("5 apples and 6 oranges", 19))
```
The output should be:
```
8
```