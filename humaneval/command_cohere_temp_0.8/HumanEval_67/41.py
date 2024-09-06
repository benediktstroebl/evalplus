```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operationally designed to calculate the number of mangoes in a basket of fruits. The function takes in two parameters, a string representing the total number of apples and oranges in the basket, and an integer representing the total number of fruits in the basket. 

The script splits the provided string into two integers representing the number of apples and oranges through the use of the `map` function and the `split `function. By subtracting the number of apples and oranges from the total number of fruits in the basket, the function then returns the number of mangoes in the basket. 

The function eliminates the need for manual calculations and provides a quick and accurate solution. It assumes that any negative values returned are indicative of an incorrect input or an error in the function.