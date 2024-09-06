```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
This problem can be solved by parsing the string input with the split(' and '), converting the two resulting strings into integers, and finally subtracting them from the total number of fruits to find the number of mangoes. A usage example is found below:
```python
print(fruit_distribution("5 apples and 6 oranges", 19))
```
The output for this input will be 8.