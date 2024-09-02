
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # TODO:
    #   Implement this function to return the correct answer.
    #
    # Note that the list comprehension syntax is equivalent to:
    #   answer = []
    #   for x in range(a, b+1):
    #     if x % 2 == 0:
    #       answer.append(x)
    #   return answer
    if a > b:
        return []
    else:
        answer = []
        for x in range(a, b + 1):
            if x % 2 == 0:
                answer.append(x)
        return answer

