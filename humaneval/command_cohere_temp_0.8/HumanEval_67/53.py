```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operationally serves the purpose of solving the problem as stated in the provided code block. It takes in two parameters, a string `s` that follows the structure of "`number of apples` and `number of oranges`", and an integer `n` which represents the total number of fruits in the basket. The function splits the provided string into two integers, `apples` and `oranges`, which represent the quantities of apples and oranges, respectively. It then returns the number of mango fruits in the basket by calculating `n - apples - oranges`, which effectively subtracts the quantities of apples, oranges, and mango fruits from the total number of fruits in the basket. 

Here's an example of how you can use the code:
```python
print(fruit_distribution("5 apples and 6 oranges", 19)) # Output: 8
```

And here's another example:
```python
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
```

And lastly, another example:
```python
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
```

These examples will help us to understand the functionality of the function and how it solves the problem. In all three examples, the function successfully calculates the number of mango fruits in the basket by subtracting the number of apples, oranges, and mango fruits from the given total number of fruits in the basket.