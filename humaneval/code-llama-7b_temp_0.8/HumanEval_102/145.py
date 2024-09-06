
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # First, I'll check if x and y are integers. If they're not, then I return 
    # -1.
    if not isinstance(x, int) or not isinstance(y, int):
        return -1

    # If x and y are integers, then I check if they're positive. If x and y are 
    # negative, then I return -1.
    if x < 0 or y < 0:
        return -1

    # If x and y are positive, then I check if x is smaller than y, if it's 
    # not, then I swap the numbers.
    if x > y:
        x, y = y, x

    # Now I'll loop through the numbers in the range [x, y] inclusive, and 
    # check if it's divisible by 2. If it is, then I assign it to the variable 
    # biggest_even. 
    biggest_even = -1
    for i in range(x, y + 1):
        if i % 2 == 0 and i > biggest_even:
            biggest_even = i

    # Finally, I return the variable biggest_even.
    return biggest_even
