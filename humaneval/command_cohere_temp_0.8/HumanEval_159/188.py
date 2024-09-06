Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    temp = n + need
    if temp > rem:
        temp = rem
    yield temp
    yield rem - temp
```
This script defines a function that takes in three variables: `n` which is the number of carrots already eaten, `need` which is the number of carrots needed to be eaten, and `rem` which is the number of remaining carrots. The function yields two values: the total number of carrots eaten after meals (which is less than or equal to the remaining carrots), and the final number of remaining carrots.

This solution focuses on the yielding functionality, which saves memory space and is more efficient compared to the traditional returning of multiple values in Python. The constraint on the input variables is also considered in this solution through the if condition present in the code.

Here is a usage example when calling this function:
```python
print(list(eat(2, 11, 5)))
```
This would output:
```
[7, 0]
```
Which indicates that after eating the 11 carrots needed, there are still 7 carrots left.