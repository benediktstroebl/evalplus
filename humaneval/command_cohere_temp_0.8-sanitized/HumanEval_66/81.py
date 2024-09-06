def digitSum(s):
    return sum(map(int, list(filter(str.isdigit, s))))