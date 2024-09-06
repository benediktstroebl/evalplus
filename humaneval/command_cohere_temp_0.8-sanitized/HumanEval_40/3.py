def triples_sum_to_zero(lst):
    # Write your code here. Read the markdown for more details.
    return len(set(zip(lst, lst[1:], lst[2:] + [None]))) == 3 and all(a + b + c == 0 for a, b, c in zip(lst, lst[1:], lst[2:] + [None]))