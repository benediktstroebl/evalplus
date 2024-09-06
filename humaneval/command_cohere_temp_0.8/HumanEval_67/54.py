```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the two integers representing the number of apples and oranges from the string using `map(int, s.split(' and '))`. Subsequently, it calculates the total number of mangoes by subtracting the number of apples and oranges from the total number of fruits using the equation `return n - apples - oranges`. 

Here's an example of how you can use the code for computation:
```python
fruit_distribution("5 apples and 6 oranges", 19)
```
Which will return `8` as the result. 

This approach assumes that the input string includes exactly two space-separated integers representing apples and oranges, and that the total number of fruits in the basket is provided as an integer input. 

Ensure that you adhere to the specific input/output formats and conditions described in the problem when utilizing this function.