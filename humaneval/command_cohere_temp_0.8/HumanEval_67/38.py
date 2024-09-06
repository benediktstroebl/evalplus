```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code solves the problem by taking the input string s that represents the number of apples and oranges in a particular format and converting it into integer values `apples` and `oranges` using the `map` function. It then returns the number of mangoes based on the formula `n - apples - oranges`, where `n` represents the total number of fruits in the basket. The code elegantly splits the input string and directly computes the result without the need for explicit loops or intermediate variables. 

This code is concise and straightforward, making it easily understandable and adaptable to varying input scenarios.