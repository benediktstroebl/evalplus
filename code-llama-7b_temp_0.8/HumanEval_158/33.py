
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Write your code here.
    # 创建一个用于统计每个单词中的字母个数的字典
    # 统计次数最高的单词
    # 如果有多个单词，先根据字母个数排序
    # 如果有相同的单词，根据字母的字典序排序
    count_map = {}
    max_count = -1
    max_word = ''
    for word in words:
        char_set = set()
        for char in word:
            char_set.add(char)
        count = len(char_set)
        if count > max_count:
            max_count = count
            max_word = word
    return max_word
