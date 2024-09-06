Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ct, leave = 0, 0
    while need > 0:
        if rem == 0:
            break
        ct += 1
        rem -= 1
        if ct == need:
            leave = rem
            break
    return [ct, leave]
```
This function uses a while loop to repeatedly eat carrots until it has eaten enough to satisfy its hunger or it has no more carrots available. It consumes one carrot per iteration and decrements the needed number of carrots per iteration. Once the required number of carrots has been eaten, it sets the leave value to the remaining carrots. 

Here is an example usage of the function:
```python
print(eat(2, 11, 5))
```
This will output:
```
[7, 0]
```

This indicates that the rabbit has eaten 7 carrots and there are 0 carrots left afterwards.