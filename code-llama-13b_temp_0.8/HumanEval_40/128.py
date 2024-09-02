

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    # new_list = list(l)
    # i = 0
    # for num in l:
    #     while i < len(new_list):
    #         if i == i:
    #             i += 1
    #             continue
    #         if new_list[i] + num + new_list[i] == 0:
    #             return True
    #         else:
    #             i += 1
    # return False
    # new_list = []
    # for number in l:
    #     new_list.append(number)
    #     for num in l:
    #         for num_two in l:
    #             if num + num_two + number == 0:
    #                 return True
    # return False

    # my_list = set(l)
    # for num in l:
    #     if (-1 * num) in my_list:
    #         return True
    # return False
    # i = 0
    # j = 0
    # for num in l:
    #     for num_two in l[i + 1:]:
    #         for num_three in l[j + 2:]:
    #             if num + num_two + num_three == 0:
    #                 return True
    #             else:
    #                 j += 1
    #         j = i + 1
    #         i += 1
    # return False
    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False
