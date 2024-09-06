
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    vowel = ['A', 'E', 'I', 'O', 'U']
    n = len(word)
    # 拿到右边第一个非字母的地方
    for i in range(n-1, -1, -1):
        if not word[i].isalpha():
            # 从这个地方开始向左找
            for j in range(i-1, -1, -1):
                if word[j].isalpha():
                    if word[j].upper() in vowel:
                        # 这里就是个vowel
                        for k in range(i-1, -1, -1):
                            if word[k].isalpha():
                                return word[k]
            return ''
    return ''
    
    # 解法2
    vowel = ['A', 'E', 'I', 'O', 'U']
    n = len(word)
    for i in range(n-1, -1, -1):
        if word[i].upper() in vowel:
            for j in range(i-1, -1, -1):
                if word[j].isalpha():
                    return word[j]
    return ''
