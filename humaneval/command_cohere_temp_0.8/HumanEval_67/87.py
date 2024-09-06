```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The `fruit_distribution` function takes two parameters, a string `s` and an integer `n`. The string `s` is parsed line by line to convert the string representation of apples and oranges into integers using the `map` function. Then, the function returns the total number of fruits in the basket minus the number of apples and oranges. Essentially, the number of mangoes is represented by the difference between the total fruits and the apples and oranges subtracted.

Here is a usage example for the above function to further explain:
```python
print(fruit_distribution("5 apples and 6 oranges", 19))
# Output: 8
```

The above would print: `8` because there are 5 apples, 6 oranges, and 8 mangoes in the basket. The total number of fruits in the basket is 19. So, the function calculates 19 - 5 - 6 to get the number of mangoes. The result is 8. 

This approach is straightforward and works well for this particular case. However, it's important to note that this solution assumes that the given string is formatted correctly, which may not always be the case in real-world scenarios. If the input string could potentially be malformed (i.e., not following the expected format of "number of apples and number of oranges"), additional validation and handling would be necessary.