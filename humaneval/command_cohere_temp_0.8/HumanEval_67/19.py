```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the two integers representing the number of apples and oranges from the string using **map()** and **.split(' and ')** to separate the two integers. Then, by simply subtracting the sum of apples and oranges from the total number of fruits, **fruits_distribution** returns the number of mangoes. 

For better readability, the function could be enhanced by using **dict** and **lambda** to convert strings to integers:
```python
def fruit_distribution(s,n):
    d = {'apples': lambda: int(x) for x in s.split(' and ')}
    return n - sum(d[k]()) for k in d if d[k]()>0
```

Which uses a **dict** with string keys and **lambda** functions as values to convert each string in the list to its corresponding integer value.

With the converted integers, the function then returns the number of mangoes by subtracting the sum of apples and oranges from the total number of fruits. 

Both approaches correctly solve the problem but having **map()** and **lambda** can simplify the code and enhance readability.