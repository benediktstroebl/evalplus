

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
    # Your code here
    def check_if_number_is_pos_int(number):
        return number >= 0

    def check_if_number_is_int(number):
        return number % 1 == 0

    def check_if_number_is_in_lst(lst, number):
        return number in lst

    def round_to_upper_int_ceil(number):
        return int(number)

    def sum_squares_helper(lst, sum):
        if check_if_number_is_pos_int(lst[-1]):
            lst.append(lst[-1])
            sum += lst[-1]
            lst.pop()
            sum += lst[-1]
        else:
            lst.pop()
            sum += lst[-1]
        return sum

    result = sum_squares_helper(lst, 0)

    return round_to_upper_int_ceil(result)

test = [1,2,3,4,5]
