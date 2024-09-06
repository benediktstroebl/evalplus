```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operationally designed to solve the problem statement. The function takes in two parameters, a string `s` and an integer `n`, and it returns the number of mangoes in the basket. 

To solve the problem, the function dissects the given string using the expression `s.split(' and ')` creating a tuple with two elements denoting the number of apples and oranges. Those are then converted to integer using the `map()` function. The function finally returns the total number of fruits in the basket minus the sum of apples and oranges. 

This solution is encapsulated, where all the necessary computations are carried out within the function, making it autonomous and easy to reuse. 

This script can be embedded as is into a larger program or imported as a module to cater to a variety of problem-solving needs.