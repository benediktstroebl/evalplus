def choose_num(x, y):
    max_even = (x + y) // 2
    max_even += max_even % 2  # Make it inclusive for even numbers
    if max_even >= x and max_even <= y:
        return max_even
    return -1