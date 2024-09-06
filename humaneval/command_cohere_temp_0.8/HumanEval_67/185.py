```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operationally designed to solve the problem statement. It takes in two parameters, a string `s` and an integer `n`, which represent the combined number of apples and oranges and the total number of fruits in the basket, respectively. 

The function splits the provided string `s` into two parts using the "and" delimiter to extract the separate counts of apples and oranges. Those numbers are then converted from strings to integers using the `map` function. 

Ultimately the function calculates the number of mangoes by subtracting the combined counts of apples and oranges from the total number of fruits. This is achieved by subtracting the `apples` and `oranges` variables from the `n` variable. 

This code is a self-contained Python script that solves the given problem, as it defines the necessary function, and the only dependency is for standard Python functionality. It also outputs a valid numeric result based on the provided inputs, as required by the problem statement.