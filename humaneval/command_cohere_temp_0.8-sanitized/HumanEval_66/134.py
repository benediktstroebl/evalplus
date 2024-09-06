def digitSum(s):
    return sum(map(int, filter(str.isdigit, s)))