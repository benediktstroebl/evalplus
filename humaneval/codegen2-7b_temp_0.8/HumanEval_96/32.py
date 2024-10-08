
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
    count_dict = {x: 1 for x in range(1, n + 1)}

    for i in range(2, n + 1):
        if count_dict[i] == 1:
            count_dict[i * i] += 1
            if i * i < n + 1:
                count_dict[i * i] += 1
        else:
            count_dict[i] = 1

    return [x for x in count_dict if count_dict[x] == 1
