
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # 1. Initialize the result to an empty list
    # 2. If a is less than b, then...
    # 2a. If a is not divisible by 2, then add 1 to a
    # 2b. If b is not divisible by 2, then subtract 1 from b
    # 3. While a is less than b, add 2 to a
    # 4. Return the result

    # Test Case 1:
    #    Input:
    #        a: 2
    #        b: 8
    #    Output:
    #        RESULT: [2, 4, 6, 8]
    # 
    # Test Case 2:
    #    Input:
    #        a: 8
    #        b: 2
    #    Output:
    #        RESULT: [2, 4, 6, 8]
    # 
    # Test Case 3:
    #    Input:
    #        a: 10
    #        b: 14
    #    Output:
    #        RESULT: []

    result = []

    if a < b:
        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b -= 1

    while a < b:
        a += 2
        result.append(a)

    return result

