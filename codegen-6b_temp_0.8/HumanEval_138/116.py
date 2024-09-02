
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # n = int(n)
    n = str(n)
    if n.find('4') != -1:
        return False
    n = map(int, n)
    all_evens = [a for a in n if a % 2 == 0]
    if len(all_evens) < 4:
        return False
    all_evens.sort()
    return sum(all_evens[:4]) == sum(all_evens[4:])
