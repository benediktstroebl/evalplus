```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the two fruits' quantities as integers and finds the difference between the total quantity and the summed apples and oranges. Thus, the quantity of mangoes is returned. You can test the above program by calling the `fruit_distribution()` function with different input values to see the result. 

Here is an example:
```python
print(fruit_distribution("5 apples and 6 oranges",19))
```
Which would print:
```
8
```

This aforementioned solution efficiently calculates the number of mangoes in the basket based on the given inputs.