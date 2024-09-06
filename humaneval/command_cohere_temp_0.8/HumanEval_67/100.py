```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operationally designed to solve the problem statement. The function takes in two parameters, namely `s` and `n`, where `s` represents a string describing the distribution of apples and oranges in a basket of fruit, and `n` is an integer representing the total number of fruits in the basket. The function splits the string into an integer representing apples and another integer representing oranges using the `split` method. It then calculates the number of mangoes by subtracting the number of apples and oranges from the total number of fruits in the basket, and returns this difference. 

The code is self-contained and does not rely on any external variables or functions, and matches the required functionality to solve the given problem. I hope this helps! Let me know if you would like me to explain anything else about the code.