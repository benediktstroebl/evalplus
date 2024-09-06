import unittest
def odd_count(lst):
    return [str(len(re.findall(r'1|3|5|7|9', s))) for s in lst]