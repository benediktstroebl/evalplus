
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # positive even number has to be divisible by 4.
    if n % 4 != 0:
        return False

    # Initialise a list of even numbers, whose sum would be equal to the given n
    numbers = [2]

    # Keep adding the next even number to the list until the sum of the list elements is greater than n
    while sum(numbers) <= n:
        # Calculate the next even number
        next_number = numbers[-1] + 2
        # If the next number is greater than n, break the loop
        if next_number > n:
            break
        # Otherwise, add the next number to the list
        numbers.append(next_number)

    # If the last sum is equal to n, return True, otherwise, return False
    return sum(numbers) == n

