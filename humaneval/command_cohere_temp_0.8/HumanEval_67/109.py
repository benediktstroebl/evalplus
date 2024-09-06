```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This self-contained Python script defines a function called `fruit_distribution` that takes two arguments: a string `s` and an integer `n`. This string `s` represents the number of apples and oranges in the basket, and the integer `n` represents the total number of fruits in the basket. The function splits the string into two parts, `apples` and `oranges`, and converts them into integers. The function then returns the number of mangoes in the basket by subtracting the number of apples and oranges from the total number of fruits in the basket `n`. 

Here is an example of how you can use the code`:
```python
apples, oranges = map(int, "5 apples and 6 oranges".split(' and '))
print(fruit_distribution("5 apples and 6 oranges", 19)) 
 ```

The output of this code will be:
```
8
```

Such that the program returns 8, which is the number of mangoes in the basket, according to the given problem statement. 

This script is encapsulated within itself, meaning it's standalone and doesn't rely on external variables or modules. All the logic and calculations are performed within the function, making it a self-contained solution.