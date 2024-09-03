```python
def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    
    If:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number: integer, representing the number of carrots eaten.
    @need: integer, representing the number of carrots needed.
    @remaining: integer, representing the number of remaining carrots in stock
    
    Constraints:
    - @number, @need, @remaining are integers within the range [0, 1000].
    
    Returns: tuple of two integers, representing the total number of eaten carrots and the remaining number of carrots.

Example:
>>> eat(5, 6, 10)
[11, 4]
```