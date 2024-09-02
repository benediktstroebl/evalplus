
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n % 2!= 0: # If the given number is not even, return False
        return False
    even_numbers = [2] # Save the list of positive even numbers
    for i in range(2, n):
        if i % 2 == 0 and i!= 2 and i + 2 <= n:
            even_numbers.append(i)
            even_numbers.append(i + 2)
        else:
            continue
    return sum(even_numbers) == n
