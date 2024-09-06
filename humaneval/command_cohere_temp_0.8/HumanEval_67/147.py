```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the total number of fruits in the basket as a parameter and then separates the number of apples and oranges by their respective names. It then calculates the number of mangoes by subtracting the sum of apples and oranges from the total number of fruits and returns the result. 

This approach ensures a straightforward solution to the problem that is both efficient and easy to understand. 

The `fruit_distribution` function can be utilized to solve the problem as shown in the code snippet below:
```python
# No. of fruits in the basket
n = int(input())

# Total no. of apples and oranges
s = input()

# Finding the number of mango fruits from the basket
no_of_mangoes = fruit_distribution(s, n)
print(no_of_mangoes)
```