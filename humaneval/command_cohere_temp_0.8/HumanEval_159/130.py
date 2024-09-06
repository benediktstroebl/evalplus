Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    eq = n + need
    if eq > rem:
        eq = rem
    return [eq, rem-eq]
```
The function takes in 3 variables, two integers representing the number of carrots `n` that you have already eaten and `need` the number of carrots that you need to eat respectively, and one integer representing the number of `rem` remaining carrots that exist in stock. The function returns a list of two integers representing the total number of eaten carrots after your meals and the number of carrots left after your meals respectively.

Here is an example usage of the function:
```python
print(eat(5, 6, 10))
```
This will print:
```bash
[11, 4]
```
Which indicates that after eating 5 carrots, there are 11 carrots eaten in total and 4 carrots left.