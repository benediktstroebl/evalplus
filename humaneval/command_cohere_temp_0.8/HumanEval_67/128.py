```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operationally designed to solve the problem statement. It functionally takes in two parameters, a string `s` and an integer `n`, and adheres to the problem's guidelines. The function splits the provided string `s` into two parts, yielding integers representing the number of apples and oranges, respectively. By subtraction, it calculates the total number of mango fruits in the basket, which represents the difference between the total number of fruits (`n`) and the combined count of apples and oranges. 

This solution, expressed concisely in a single line of Python, offers an efficient and direct way to determine the distribution of mango fruits in the basket based on the provided information about apples, oranges, and the total count.