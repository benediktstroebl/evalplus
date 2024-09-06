Here's a Python script that contains a function eat() that solves the given problem:
```python
def eat(n, need, rem):
    ct, leftovers = 0, 0
    while need:
        if need > rem:
            leftovers = 0
            ct += rem
            need -= rem
        else:
            ct += need
            leftovers = rem - need
        rem = 0
    return [ct, leftovers]
```

This function works in iterations. At each step, it calculates the number of carrots to be eaten from the remaining stock to meet the 'need' requirement while ensuring that not more than the available 'remaining' is eaten. The while loop continues this calculation till the 'need' is zero, indicating that all required eating has been accomplished. The function finally returns a list [total eaten carrots, remaining carrots after the meal].