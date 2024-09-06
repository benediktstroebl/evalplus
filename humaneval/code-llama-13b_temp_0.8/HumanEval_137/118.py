
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    # 테스트 1-2: 3 == compare_one(3, 3)
    # 테스트 3-4: "3" == compare_one("3", "3")
    # 테스트 5-6: "1,1" == compare_one("1,1", "1.1")
    # 테스트 7-8: None == compare_one(1, "1")
    # 테스트 9-10: None == compare_one("1", 1)

    # 테스트 1-4: 6 == compare_one(6, 6)
    # 테스트 5-8: 1.2 == compare_one(1.2, 1.2)
    # 테스트 9-12: None == compare_one(1.2, 1.2)

    # return None if the values are equal.
    if a == b:
        return None
    #
    if a > b:
        return a
    return b

