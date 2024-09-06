
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n >= 4:
        for i in range(3, n+1, 2):
            if n % i == 0:
                return False
        return True

x = 24
y = 30
result = is_equal_to_sum_even(x)
if result:
    print("y is not divisible by x")
else:
    print("y is divisible by x")
