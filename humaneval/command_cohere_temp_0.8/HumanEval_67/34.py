```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operates on two parameters, a string, and an integer. The string represents the number of apples and oranges in a basket of fruits, separated by the word "and". The function extracts the integer representations of the apples and oranges from the string using the `map` function, which transforms the string into a list of integers. Subsequently, the function subtracts these values from the total number of fruits in the basket to determine the number of mango fruits in the basket. This calculation is performed by subtracting the number of apples and oranges from the total number of fruits, resulting in the number of mango fruits in the basket. 

The function returns the number of mango fruits in the basket based on the given information about the distribution of apples and oranges.