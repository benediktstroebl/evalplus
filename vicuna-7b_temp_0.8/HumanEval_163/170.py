
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # We use two pointers, one for the left and one for the right,
    # and we alternate between them.
    # If one of the pointers reach the other, we know that we've reached the end.
    # The first non-zero digit is the first odd digit.
    while True:
        # Try to find the first non-zero digit.
        digit = 0
        while a <= b and digit == 0:
            digit = (a + b) // 2 % 10
            a, b = b, (a + b) // 2
        if digit == 0:
            # If we didn't find any non-zero digits, we're done.
            return []
        a, b = b, a
        # We now have the first odd digit.
        # Use the binary search algorithm to find the rest of the even digits.
        mid = (a + b) // 2
        left = max(a, mid - 1)
        right = min(b, mid + 1)
        while left <= right:
            # We check if the current digit is even and if the next digit is
            # greater than or equal to the current digit.
            # If so, we know that the current digit is not the first digit
            # of the block.
            if mid - left + 1 <= right - left:
                continue
            if mid - left + 1 % 10 < right - left + 1 % 10:
                continue
            if mid - left + 1 % 10 > (right - left + 1) // 2:
                continue
            # We have found the start of a new block.
            # We return the range from the start of the block to the next block.
            return [str(i) for i in range(left, mid)]
        # We haven't found any even digits, so we return an empty list.
        return []
