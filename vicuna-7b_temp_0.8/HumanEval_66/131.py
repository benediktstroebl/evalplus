
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    # 检查字符串是否为空字符串
    if s == "":
        return 0
    
    # 拆分字符串为每一个字母
    words = s.split()
    
    # 存储每个字母的 ASCII 码
    codes = {}
    for code in words:
        if code in codes:
            codes[code] += 1
        else:
            codes[code] = 1
    
    # 计算每个字母的 ASCII 码
    sum = 0
    for code, value in codes.items():
        sum += value
    
    # 返回结果
    return sum
