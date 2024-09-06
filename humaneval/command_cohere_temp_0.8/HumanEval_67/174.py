```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the two integers representing the number of apples and oranges from the string using `map(int, s.split(' and '))`. Then, the function returns the number of mangoes by subtracting the sum of apples and oranges from the total number of fruits. This solution follows theOID (Object-Oriented Design) principle, which states that "Objects should be open for extension but closed for modification." The function does not change and can be used multiple times in different parts of the code without worrying about its consistency.