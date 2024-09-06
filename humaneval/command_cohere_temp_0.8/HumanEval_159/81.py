Here's a Python script that contains a function eat() that solves the problem described in the code block above:
```python
def eat(n, need, rem):
    ct = n + need
    rt = rem >= ct ? ct : rem
    return [ct, rt]
```
This function takes in the three variables described in the prompt, eats the specified amount of carrots based on the inputs, and then returns a list with the total amount of carrots eaten and the amount of carrots left over after eating.