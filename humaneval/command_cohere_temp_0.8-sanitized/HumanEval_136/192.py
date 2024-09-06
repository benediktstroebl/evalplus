def largest_smallest_integers(lst: list) -> tuple:
    """
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.
    """
    positive: int = min(x for x in lst if x > 0)
    negative: int = max(x for x in lst if x < 0)
    return negative, positive