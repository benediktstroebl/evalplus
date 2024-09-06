
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

    
    sentence = sentence.split()
    ans = ""
    for word in sentence:
        if len(word) > 0:
            count = 0
            for letter in word:
                if not letter.isalpha():
                    count += 1
            if count == 0:
                if len(word) > 1 and len(word) % 2 == 1:
                    ans += word[len(word)//2] +''
                else:
                    for letter in word:
                        ans += letter +''
                    ans = ans[:-1]
    return ans
