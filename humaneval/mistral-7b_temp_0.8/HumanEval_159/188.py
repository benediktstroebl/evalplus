
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

    # Base cases
    # if need <= number, then you've already eaten enough carrots
    # if need >= remaining, then there aren't enough carrots to eat
    #if remaining == 0, you've eaten all the carrots
    # if number == 0, you haven't eaten any carrots

    # Main recursive cases
    # if number < remaining, then you can still eat some of the remaining carrots
    # if number + remaining >= need, then you can eat some of the remaining carrots
    # if need < number, then you've already eaten more carrots than you needed
    # if need < remaining, then there are still some carrots left to eat after you've eaten your meal

    # Write your code here!

    # print('Base Case:')
    # print(f'eaten: {number}, need: {need}, remaining: {remaining}')

    # if need <= number:
    #     return [number, 0]

    # elif need >= remaining:
    #     return [number, remaining
