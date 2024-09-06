
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
    from collections import deque
    queue = deque()
    has_vowel = False
    for i in range(len(word)):
        c = word[i]
        if c.isalpha():
            if c in 'aeiou':
                queue.appendleft(c)
                has_vowel = True
            else:
                queue.append(c)
        else:
            if has_vowel:
                char_deque = deque(queue)
                char_deque.popleft()
                queue.clear()
                queue.appendleft(char_deque.pop())
    if not has_vowel:
        return ''
    return queue.pop()
