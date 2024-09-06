
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

    s = sentence.split()
    result = ""
    for word in s:
        for i in range(2, int(len(word) / 2) + 1):
            if len(word) % i!= 0:
                continue
            if len(word) == i:
                result += word
                break
            else:
                new_word = word[0:i]
                if len(new_word) == i:
                    result += new_word
                    break
        else:
            result += word
        result += " "
    return result[:-1]
