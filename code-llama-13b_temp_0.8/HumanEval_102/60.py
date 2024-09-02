
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # We will assume the answer is the lower value, i.e. x
    answer = x

    # First we check if both values are positive
    if x > 0 and y > 0:

        # Then we check if x is even
        if x % 2 == 0:
            # If x is even we check if y is bigger than x and even
            if y >= x and y % 2 == 0:
                # If both of these are true we assign the greater value to the answer
                answer = y
            else:
                # If y is smaller than x or is not even, we check if y is bigger than x-2
                if y >= x-2:
                    # If it is, we assign the greater value to the answer
                    answer = y

        else:
            # If x is not even, we check if y is bigger than x+1 and even
            if y >= x+1 and y % 2 == 0:
                # If both of these are true we assign the greater value to the answer
                answer = y

        # In the end we return the answer
        return answer

    else:
        # If any of the two values are not positive we return -1
        return -1

