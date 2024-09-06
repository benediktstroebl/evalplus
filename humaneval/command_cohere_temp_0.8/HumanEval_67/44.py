```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the total number of fruits (`n`) and splits the input string into the number of apples and oranges using the `split(' and ')` method. It then simply subtracts the sum of apples and oranges from the total number of fruits to get the number of mangoes. This method is straightforward and works correctly for the given problem statement. It assumes that the inputs are well-formed, i.e., the string represents integer values for apples, oranges, and the total number of fruits.