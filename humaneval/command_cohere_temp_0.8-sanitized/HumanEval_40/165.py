def triples_sum_to_zero(lst):
    # Write your code here. Read the entire file and test your solution with the tests.
    return len(set(zip(lst, lst[1:], lst[2:] + [0]))
                 ) == 1 and all(a + b + c == 0 for a, b, c in set(zip(lst, lst[1:], lst[2:] + [0])))