def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x + 1)
l = [5, 6, 3, 4]