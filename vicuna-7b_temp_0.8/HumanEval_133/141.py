

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    def is_number(x):
        return x.isdigit()

    def is_positive_number(x):
        return x.isdigit() and x >= 0

    def is_neg_or_zero(x):
        return x.isdigit() and x < 0 or x == 0

    def is_int(x):
        return x.isdigit() and int(x) == x

    numbers = filter(is_number, lst)

    sum_of_squares = 0

    for num in numbers:
        num = int(num)
        if is_positive_number(num):
            sum_of_squares += num ** 2
        elif is_neg_or_zero(num):
            if is_int(num):
                sum_of_squares += abs(num ** 2)
            else:
                sum_of_squares += num ** 2
        else:
            return "Invalid input"
    return round(sum_of_squares, 2)
