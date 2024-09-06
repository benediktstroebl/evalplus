
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    d={}
    for i in words:
        for j in i:
            if j not in d:
                d[j]=0
            d[j]+=1
    max_dict=d.copy()
    max_dict=max(max_dict.items(), key=lambda x:x[1])
    for key,value in d.items():
        if value==max_dict[1]:
            if key < max_dict[0]:
                max_dict=[key,max_dict[1]]
    return max_dict[0]
