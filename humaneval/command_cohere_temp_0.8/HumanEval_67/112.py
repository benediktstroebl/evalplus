```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This script takes the input string and splits it into an array of apples and oranges. Then it calculates the number of mangoes by subtracting the number of apples and oranges from the total number of fruits. It ensures the correct output and aligns with the problem's statement as it is a direct implementation. 

### Here is the separated markdown code block:
```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```