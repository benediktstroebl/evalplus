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
    if type(a) is not type(b):
        return None
    if type(a) is str and type(b) is str and len(a) == len(b) and a == b:
        return None
    if type(a) is float or type(a) is int:
        return a if a > b else b
    elif type(a) is str and type(b) is float:
        if a.find('.') != -1:
            arr = list(map(float, a.split('.')))
            arr.reverse()
            for i in range(len(arr)):
                if arr[i] < b:
                    return b
        elif a.find(',') != -1:
            arr = list(map(float, a.split(',')))
            arr.reverse()
            for i in range(len(arr)):
                if arr[i] < b:
                    return b
        return a
    elif type(a) is float and type(b) is str:
        if b.find('.') != -1:
            arr = list(map(float, b.split('.')))
            arr.reverse()
            for i in range(len(arr)):
                if a < arr[i]:
                    return a
        elif b.find(',') != -1:
            arr = list(map(float, b.split(',')))
            arr.reverse()
            for i in range(len(arr)):
                if a < arr[i]:
                    return a
        return b
    else: 
        return a if a > b else b