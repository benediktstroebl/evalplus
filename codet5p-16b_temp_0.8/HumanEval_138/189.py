
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    
    n_list = []
    sum_even_list = []
    for i in range(1, n + 1):
        n_list.append(i)
    for i in n_list:
        if i % 2 == 0:
            sum_even_list.append(i)
    
    if len(sum_even_list) == 4:
        return True
    else:
        return False
        
        
