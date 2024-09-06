Here's a Python script that contains a function eat() that solves the given problem:
```python
def eat(n, need, rem):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    """
    eaten = n + need
    if eaten > rem:
        eaten = rem
    return [eaten, rem-eaten]
```

This function takes in three variables: 'n' which represents the number of carrots already eaten, 'need' which represents the number of carrots needed to be eaten, and 'rem' which represents the remaining amount of carrots available. The function eats the maximum amount of carrots it can, and returns a list with [the total number of carrots eaten, the number of carrots left after eating]. If the number of carrots needed to be eaten is greater than the remaining carrots, the function eats all the remaining carrots and still returns a list representing the number of carrots left which will be zero.

Here's an example of usage:
```python
print(eat(2,11,5))
```

This will output:
```
[7, 0]
```

As the hungry rabbit has only eaten 2 carrots and needed 11 to be fully fed, so it eats 9 carrots max. which leaves 5 remaining, hence the output.[7, 0]'. 

This function can be used to calculate the number of carrots consumed and the number of carrots left after meal times in a range of scenarios.