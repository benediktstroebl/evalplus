
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    number_list = []
    for i in range(1, n + 1):
        number_list.append(i)
    even_numbers = [x for x in number_list if x % 2 == 0]
    odd_numbers = [x for x in number_list if x % 2 != 0]
    even_numbers.sort()
    odd_numbers.sort()

    if len(even_numbers) == 4:
        if even_numbers[0] + even_numbers[1] + even_numbers[2] + even_numbers[3] == n:
            return True
        else:
            return False
    if len(odd_numbers) == 4:
        if odd_numbers[0] + odd_numbers[1] + odd_numbers[2] + odd_numbers[3] == n:
            return True
        else:
            return False
    else:
        return False
