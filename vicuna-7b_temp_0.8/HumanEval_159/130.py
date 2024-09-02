
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
    # Initialize a dictionary to count the number of carrots of each color
    carrot_count = { 'red': 0, 'green': 0, 'purple': 0 }

    # Eat the remaining carrots
    for i in range(remaining):
        if carrot_count['green'] >= need and carrot_count['purple'] >= need:
            carrot_count['purple'] -= need
            carrot_count['green'] -= need
            break
        elif carrot_count['red'] >= need:
            carrot_count['red'] -= need
            break
    
    # Print the result
    print("After eating", need, "carrots:")
    print(carrot_count)

    # Print the remaining carrots
    remaining_carrots = remaining - need
    print("There are", remaining_carrots, "remaining carrots.")