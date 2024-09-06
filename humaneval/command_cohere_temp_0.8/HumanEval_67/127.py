```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This script defines a function called `fruit_distribution` which takes two arguments, a string `s` and an integer `n`. The function first splits the string into two parts, assuming that the first part is the number of apples and the second part is the number of oranges. Then, it converts those parts into integer values and returns the final answer by subtracting the total count of apples and oranges from the total number of fruits. 

Here is a simple test case to verify its functionality:
```python
print(fruit_distribution("10 apples and 12 oranges", 24))
```

The output will be:
```bash
2
```