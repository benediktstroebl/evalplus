
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    list_of_odds = []
    for i in range(2, n):
        if i % 2 == 1:
            list_of_odds.append(i)
    list_of_odds.sort()
    for i in list_of_odds:
        if n - i not in list_of_odds:
            return False
        else:
            list_of_odds.remove(n - i)
    if sum(list_of_odds)!= 0:
        return False
    else:
        return True
    return False
