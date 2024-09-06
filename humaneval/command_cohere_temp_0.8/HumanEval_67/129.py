```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The script uses the split method to split the string into individual parts and then uses the map function to convert these parts into integers. It then returns the total number of fruits in the basket less the number of apples and oranges. This follows the logic that the number of mangoes is the total amount of fruits in the basket minus the known amounts of apples and oranges. 

Here's an example usage of the function for clarity:
```python
print(fruit_distribution("5 apples and 6 oranges", 19))
```
Which should output:
```bash
8
```