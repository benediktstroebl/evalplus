
def eat(number, need, remaining):
    """
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
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
    # write your code here
    a = int(number / 100)
    b = int((number % 100) / 10)
    c = int((number % 10) / 1)

    while need > 0:
        if remaining < c:
            break
        remaining -= c
        need -= c
        if remaining == 0:
            break
        number -= c
        a += 1
        if a == 100:
            remaining += 100
            a = 0
        b += 1
        if b == 10:
            remaining += 100
            b = 0
        c += 1

    return [a, b, c, remaining]