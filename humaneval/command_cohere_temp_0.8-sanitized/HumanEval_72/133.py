import unittest
def will_it_fly(q, w):
    return (len(q) > 1 and q == q[::-1] and sum(q) <= w)