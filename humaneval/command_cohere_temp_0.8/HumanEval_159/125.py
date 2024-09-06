Here's a Python script that contains a function named `eat` which solves the given problem:
```python
def eat(n, need, rem):
    ate = n + min(need, rem)
    rem = max(0, rem - need)
    return [ate, rem]
```
This function uses three parameters: `n` represents the number of carrots already eaten, `need` represents the number of carrots needed to be eaten, and `rem` represents the remaining number of carrots. 

The function returns a list `[total ate, remaining rem]`, where `ate` is the total number of carrots eaten (including the initial number eaten), and `rem` is the number of carrots left after eating. 

The function uses the `min` and `max` functions to ensure that the number of carrots eaten is less than or equal to the remaining carrots. Also, if the number of carrots needed to be eaten is larger than the remaining carrots, the function will eat all remaining carrots, but will still be hungry (return remaining carrots as 0).

Here is an example usage of the function:
```python
print(eat(5, 6, 10))
# Output: [11, 4]

print(eat(4, 8, 9))
# Output: [12, 1]

print(eat(1, 10, 10))
# Output: [11, 0]

print(eat(2, 11, 5))
# Output: [7, 0]
```

This script will produce the desired output as shown in the example usage section above which corresponds to the specified problem.