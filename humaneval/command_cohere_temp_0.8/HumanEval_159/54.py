Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    return [n + min(need, rem), max(0, rem - need)]
```
This function uses the `min` function to ensure that the rabbit eats enough carrots to meet its needs, even if it has to eat all the remaining carrots. It also ensures that the number of carrots left is not negative (i.e., zero or more). 

Here is an example to demonstrate the use of the function:
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

This script will output the expected results based on the provided example in the problem statement.