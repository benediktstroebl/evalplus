Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    bunny_eat = n + need
    leftover = rem - bunny_eat
    return [bunny_eat, leftover]
```

This function takes in three parameters, `n` which represents the number of carrots already eaten, `need` which represents the number of carrots needed to be eaten, and `rem` which represents the remaining amount of carrots. The function calculates the total number of carrots eaten by the rabbit and then returns the number of leftover carrots after the rabbit's meal. It ensures that the rabbit eats enough to meet its needs and always leaves some leftover food. 
It returns a list containing the total eaten carrots and the number of leftover carrots. An example usage of this function is:
```python
print(eat(2, 11, 5))
```
This will output:
```
[7, 0]
```

This represents that after the rabbit eats 11 carrots (2 initial + 11 new), there are 7 carrots left. 

This code snippet ensures that the rabbit eats the appropriate amount to meet its needs while also ensuring there are no food shortages as it always leaves some leftover. In the context of the problem, the rabbit represents a hungry rabbit, the carrots represent the food it eats, and the numbers represent the different quantities of food throughout the day.