def multiply(a, b):
    return int(str(a) + str(b)) * 10 ** min(len(str(a)), len(str(b)))