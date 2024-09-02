
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    sentence = sentence.upper()
    words = sentence.split()
    new_words = []
    for word in words:
        if len(word) > 1:
            new_words.append(word)
    new_words = sorted(new_words, key=len, reverse=True)
    for i in range(1, len(new_words)):
        for j in range(i + 1, len(new_words)):
            if new_words[i] > new_words[j]:
                new_words[i], new_words[j] = new_words[j], new_words[i]
                break
    return ' '.join(new_words)

test = [
    ["aaa", "bbb", "ccc"],
    ["ddd", "eee", "fff"],
    ["ggg", "hhh", "iii"],
    ["jjj", "kkk", "lll"],
    ["mmm", "nnn", "ooo"],
    ["ppp", "qqq", "rrr"],
    ["ttt", "uuu", "vvv"],
    ["www", "xxx", "yyy"],
    ["zzz", "www", "xxx"]
]

for i in test:
    print("Case ", i+1, ": ", words_in_sentence(i[0]))