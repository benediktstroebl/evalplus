def make_a_pile(n):
    """
    Construct a pile of stones with n levels following the problem statement.
    """
    result = []
    if n % 2 == 1:  # Odd number of stones in the first level
        current_stones = n
        while current_stones != 1:
            result.append(current_stones)
            current_stones = (current_stones + 1) // 2  # Move to next odd number
    else:  # Even number of stones in the first level
        current_stones = n
        while current_stones > 1:
            result.append(current_stones)
            current_stones //= 2  # Move to next even number
    return result