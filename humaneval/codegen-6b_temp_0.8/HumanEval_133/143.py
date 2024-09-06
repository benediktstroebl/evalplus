

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
    # The goal is to "round" all of the elements by the function ceil.
    # Say for example lst = [1,4.2,0]
    # lst[0] is 1, lst[1] is 4.2, lst[2] is 0
    # lst[0] and lst[1] are integers: ceil(lst[0]) returns 1, ceil(lst[1]) returns 4
    # so lst[2] is unchanged, and lst[2] is not rounded to 0 (ceil(0) returns 0)
    # lst[0] and lst[1] are both rounded to 1

    # We'll need the "floor" function in the loop. It's a trick of doing arithmetic
    # with integers that rounds down. For lst = [1,4.2,0]
    # since 1**2 + 4.2**2 + 0**2 = 5.6, we'll need to round lst[0] to 4, lst[1] to 4.2,
    # and lst[2] to 0
    # the result is -3, because lst[2] is not rounded to 0.

    # So, we must do:
    # floor(lst[0]) + floor(lst[1]) + floor(lst[2]) = -3

    # Finally, we must:
    # lst[0] + lst[1] + lst[2] = -3
    # lst[0] + lst[1].ceil() + lst[2].ceil() = -3

    # So, we can find the solution by:
    # lst[0] + lst[1] + lst[2] = -3
    # lst[0] + lst[1].ceil() + lst[2].ceil() = -3
    # lst[0].ceil() + lst[1].ceil() + lst[2].ceil() = -3
    # lst[0].ceil() + lst[1].ceil().ceil() + lst[2].ceil() = -3
    # lst[0].