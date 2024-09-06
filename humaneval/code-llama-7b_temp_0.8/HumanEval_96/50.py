
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    # initialize an empty list
    result = []
    # for all the integer between 0 and n
    for i in range(n):
        # start with the first element
        if i == 0:
            continue
        # then for all the integer that are higher than 0
        else:
            # check if the integer is divisible by 2
            if i % 2 == 0:
                continue
            # check if the integer is divisible by 3
            elif i % 3 == 0:
                continue
            # check if the integer is divisible by 5
            elif i % 5 == 0:
                continue
            # if all the previous conditions are not met
            else:
                # then append the integer to the list
                result.append(i)
    return result

