from typing import List
def will_it_fly(q, w):
    return (sum(q) <= w) and (w <= len(q) == len(set(q)))
    # reverse to check for palindrome
    # return sum q <= w and len(q) == len(set q) and w >= reverse(q)