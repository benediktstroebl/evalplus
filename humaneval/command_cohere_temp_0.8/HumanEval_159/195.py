Here's a Python script that contains a function eat() that solves the problem described in the code block above:
```python
def eat(n, need, rem):
    ct, leftover = n, rem
    while need > 0:
        if leftover == 0:
            break
        temp = min(need, leftover)
        leftover -= temp
        ct++, need -= temp
    return [ct, leftover]
```
The script defines a function 'eat' takes three parameters: 'n' (number of carrots already eaten), 'need' (number of carrots needed to eat), 'rem' (remaining carrots in stock). The function returns a list containing [Total number of carrots eaten after meals, Number of carrots left after meals]. The function uses a while loop until the "need" is eaten and increments the "total eaten" with each loop. The loop minimizes the number of carrots taken from the "remaining" variable and updates the "leftover" variable accordingly.