Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ans = [n + need, max(0, rem - need)]
    return ans
```
This function uses vector addition and subtraction to calculate the total number of carrots consumed and the number of remaining carrots after the rabbit has eaten. It then uses the `max` function to ensure that the number of remaining carrots is not negative (i.e., if the rabbit eats more carrots than are currently available, it will set the remaining carrots to 0). The function returns an array containing the two values.