
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
    words = sentence.split()
    words_list = []
    i = 0
    while i < len(words)-1:
        if words[i] == " ":
            i += 1
        elif words[i] == " ":
            words_list.append(words[i])
            i += 1
        else:
            for j in range(i+1, len(words)):
                if words[i] % words[j] != 0:
                    words_list.append(words[i])
                    i += 1
                    break
            else:
                words_list.append(words[i])
                i += 1
    result = " ".join(words_list)
    return result