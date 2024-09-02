
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x < 1 or y < 1:
        return -1
    # if y > x:
    #     x, y = y, x
    re = math.ceil((x+y-1)/2)
    if re*2 == (x+y-1):
        return re
    else:
        if re*2 > x+y-1:
            return -1
        else:
            return re

test.expect(choose_num(12, 15), 14)
test.expect(choose_num(13, 12), -1)
test.expect(choose_num(0,0), -1)
test.expect(choose_num(10, 10), 10)
test.describe('Basic Tests')
test.assert_equals(choose_num(12, 15), 14)
test.assert_equals(choose_num(13, 12), -1)
test.assert_equals(choose_num(1,1), 1)
test.assert_equals(choose_num(10, 10), 10)
