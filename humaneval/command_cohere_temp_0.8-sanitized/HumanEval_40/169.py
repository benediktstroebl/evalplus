def triples_sum_to_zero(lst):
    # Write your code here. Read the markdown code block before proceeding.
    ts = tuple(zip(lst, lst[1:], lst[2:]))
    return any(sum(t) == 0 for t in ts if t[0] != t[1] and t[0] != t[2])