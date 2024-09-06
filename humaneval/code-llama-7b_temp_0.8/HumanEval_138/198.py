
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # if n%2 == 1:
    #     return False
    # elif n in [2,4]:
    #     return True
    # else:
    #     return False

    if n%2 == 1 or n in [0,1,3,5,7,9]:
        return False
    else:
        return True

    # n_string = str(n)
    # if n_string.count('1') != 0:
    #     return False
    # else:
    #     return True

    # num_list = []
    # num_list_even = []
    # while n > 0:
    #     d = n % 10
    #     n = n // 10
    #     num_list.append(d)
    # num_list.reverse()
    # for i in num_list:
    #     if i % 2 == 0:
    #         num_list_even.append(i)
    # print(num_list_even)
    # if len(num_list_even) != 4:
    #     return False
    # else:
    #     return True
