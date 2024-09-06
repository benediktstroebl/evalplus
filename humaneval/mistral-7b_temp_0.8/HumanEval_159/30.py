
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

    # NOTE: You don't need to use this variable. You can use the number of carrots that you need to eat,
    #       which is `need`.
    #       However, using `need` will have a more dynamic solution.
    #       It will be easier for you to implement the solution if you use this variable,
    #       but you will have to adjust your code if the value of `need` changes.
    #       You should use `need` in your solution if you want to have a dynamic solution.
    need_to_eat = need - number

    return [need_to_eat + remaining, remaining - need_to_eat]

