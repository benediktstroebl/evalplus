Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ate = n
    if need > rem:
        ate = rem
    print(f"You the rabbit, have eaten {ate} carrots, and have {rem} carrots remaining.")
    return [n + ate, rem - ate]
```

This script defines a function `eat(n, need, rem)` that represents a rabbit that needs to eat some carrots. The rabbit has already eaten `n` carrots, but needs to eat `need` carrots, and there are only `rem` carrots remaining in stock. The function calculates how many carrots the rabbit will eat (which cannot exceed the remaining supply), and returns a list with the total number of carrots eaten (after its meals) and the number of carrots left after its meals. 

This code should help you understand the approach to this problem. Let me know if you have any questions.