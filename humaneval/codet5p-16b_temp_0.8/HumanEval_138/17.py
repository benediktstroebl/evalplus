
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n = int(n) # makes sure the input is an integer
    if n%2!= 0: # makes sure the input is even
        return False
    sum = 0 # makes a sum variable
    for i in range(1, int((n/2)+1)): # makes a for loop that goes through all numbers less than half the input number
        if i % 2 == 0: # makes sure the number is even
            sum += i
    return sum == n
