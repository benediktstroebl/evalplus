
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    # [1,1,1,1] => 4
    # [1,1,1,2] => 4

    # [1,1,2,2] => 4

    # [1,2,2,2] => 4

    # [2,2,2,2] => 4

    # [1,1,2,2] => 4

    # [1,1,2,1] => 4

    # [1,2,1,2] => 4

    # [1,2,1,1] => 4

    # [2,1,1,1] => 4

    # [1,1,2,1,1] => 5

    # [1,1,2,2,1] => 5

    # [1,1,2,2,2] => 5

    # [1,1,2,1,1,1] => 6

    # [1,1,2,1,1,2] => 6

    # [1,1,2,1,2,2] => 6

    # [1,1,2,2,1,1] => 6

    # [1,1,2,2,1,2] => 6

    # [1,1,2,2,2,1] => 6

    # [1,1,2,2,2,2] => 6

    # [1,1,1,1,1,1,1,1] => 8

    # [1,1,1,1,1,1,1,2] => 8

    # [1,1,1,1,1,1,2,1] => 8

    # [1,1,1,1,1,2,1,1] => 8

    # [1,1,1,1,2,1,1,1] => 8

    # [1,1,1,2,1,1,1,1] => 8

    # [1,1,2,1,1,1,
