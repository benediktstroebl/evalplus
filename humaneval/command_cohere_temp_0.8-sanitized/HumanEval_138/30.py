def is_equal_to_sum_even(n):
    # Check whether the given number can be expressed as the sum of 4 even positive numbers
    # First, check if the number is less than 4
    if n < 4:
        return False
    # Secondly, check if the number is equal to the sum of 4 even numbers
    num = n
    # Check for each even positive number between 2 and num
    for i in range(2, num // 2 + 1):
        if num == i + (num - i) // 2:
            return True
    # If no combination is found, return False
    return False