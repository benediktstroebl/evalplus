def largest_smallest_integers(lst):
    if not negative_int_lst:
        return (None, None)  # No negative or positive integers
    else:
        # Find the maximum of all negative integers
        max_neg_int = max(x for x in negative_int_lst if x < 0)

        # Find the smallest of all positive integers
        min_pos_int = min(x for x in positive_int_lst if x > 0)

        return (max_neg_int, min_pos_int)
negative_int_lst = [-1, 0, 2, 3, -4]
positive_int_lst = [1, 2, 3, 4, 5]