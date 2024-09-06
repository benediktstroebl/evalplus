
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    n_list = list(str(n))
    n_list.sort()
    n_list = n_list[::-1]
    is_even_digit = False
    for digit in n_list:
        if int(digit) % 2 == 0:
            is_even_digit = True
            break
    if n % 2 != 0 or not is_even_digit:
        return False
    else:
        for i in range(len(n_list) - 1):
            for j in range(i + 1, len(n_list)):
                s = int(n_list[i]) + int(n_list[j])
                if s == int(n):
                    return True
        return False

