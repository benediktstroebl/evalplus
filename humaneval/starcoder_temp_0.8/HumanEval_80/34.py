
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

    def helper(n, visited=set()):
        if n == 1:
            return True

        visited.add(n)

        if n % 10 == 0:
            return False

        remainder = sum([int(digit)**2 for digit in str(n)])

        if remainder in visited:
            return False
        return helper(remainder, visited)

    return helper(s)
