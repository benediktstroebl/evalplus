Here's a Python script that contains a function eat() that solves the given problem:
```python
def eat(n, need, rem):
    '''
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots that exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000
    '''
    # eat all the carrots if there is not enough remaining quantity
    if need > rem:
        return [n + rem, 0]
    else: 
        # eat the needed quantity and return the remaining quantity
        return [n + need, rem - need]
```

This script defines a function `eat(n, need, rem)` that takes three parameters `n` (number of carrots already eaten), `need` (number of carrots needed), and `rem` (number of remaining carrots). The function returns a list containing the total number of carrots eaten after meals and the number of carrots left after meals. 

The logic is straightforward: if there are not enough remaining carrots to fulfill the needed quantity, the rabbit eats all the remaining carrots, indicating that it will still be hungry (as it needs more carrots). Otherwise, the rabbit eats the needed quantity, and the remaining quantity after the meal is returned alongside it. 

This solution works within the given constraints of the problem statement. You can use it with any input that adheres to the stated constraints, and it will provide you with the correct output. Feel free to use it in your project or modify it to suit your needs; if you'd like help with anything else, don't hesitate to ask!