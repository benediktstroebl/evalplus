import unittest
def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    mx, mn = max(lst), min(lst)
    return mx if mx == mn else mn + 1