Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ct = n + need
    rt = rem >= ct ? ct : rem
    return [ct, rt]
```
This function takes in 3 variables namely; `n` which is the number of carrots already eaten, `need` which is the number of carrots needed to be eaten, and `rem` which is the remaining number of carrots. The function returns a list consisting of two numbers represented by [ct, rt] where `ct` is the total number of carrots eaten and `rt` is the number of carrots left after eating. These are returned only if there are insufficient carrots, the function will eat all the remaining carrots but will still be hungry.

Here is an example usage of the function:
```python
eat(5, 6, 10)
```
This would return `[11, 4]`.

This solution is based on the following constraints:
* 0 <= number <= 1000
* 0 <= need <= 1000
* 0 <= remaining <= 1000