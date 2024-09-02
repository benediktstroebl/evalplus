
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
    def helper(i):
        if i <= 2:
            return []

        res = [2]

        j = 3
        if i % 2 == 0:
            j = 2

        while j < i:
            if i % j == 0:
                break
            j += 2
            res.append(j)

        return res + [i]

    return helper(n)

