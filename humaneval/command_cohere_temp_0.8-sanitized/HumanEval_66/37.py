def digitSum(string):
    return sum(map(int, list(filter(str.isdigit, string))))