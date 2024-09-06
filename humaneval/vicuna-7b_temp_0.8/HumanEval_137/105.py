
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
    if type(a) == type(b) and a > b:
        return a
    if type(a) != type(b):
        if type(a) == int and type(b) == float:
            return b
        elif type(a) == float and type(b) == int:
            return b
        elif type(a) == str and type(b) == str:
            return max(a.split(","), b.split(","))
        elif type(a) == str and type(b) == float:
            return max(a.split(","), float(b))
        elif type(a) == float and type(b) == str:
            return max(float(a).split(","), b)
        else:
            return None
    else:
        return None

compare_one_list = []

for i in range(1, 5):
    for j in range(i+1, 5):
        if i % 2 == 0:
            compare_one_list.append(compare_one(i, j))
        else:
            compare_one_list.append(compare_one(j, i))

for item in compare_one_list:
    if item:
        print(item)
    else:
        print(compare_one_list)