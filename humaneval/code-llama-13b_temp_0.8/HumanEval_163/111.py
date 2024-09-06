
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # your code here
    # s = ""
    # for i in range(a,b+1):
    #     s = s+str(i)
    # result = []
    # for i in s:
    #     if int(i)%2 ==0:
    #         result.append(int(i))
    # return list(set(result))

    return [num for num in range(a, b + 1) if num % 2 == 0]

