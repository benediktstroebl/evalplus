
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
    sentence = sentence.lower()
    words = sentence.split()
    result = []
    for i in range(len(words)):
        word = words[i]
        if word.isdigit():
            result.append(word)
        else:
            prime = True
            for j in range(i+1, len(words)):
                if word == words[j] and (words[j-1] == "a" or words[j-1] == "an" or words[j-1] == "the" or words[j-1] == "and" or words[j-1] == "but" or words[j-1] == "or" or words[j-1] == "so" or words[j-1] == "nor" or words[j-1] == "there" or words[j-1] == "was" or words[j-1] == "have" or words[j-1] == "all" or words[j-1] == "to" or words[j-1] == "with" or words[j-1] == "out" or words[j-1] == "for" or words[j-1] == "on" or words[j-1] == "at" or words[j-1] == "into" or words[j-1] == "back" or words[j-1] == "off" or words[j-1] == "over" or words[j-1] == "into" or words[j-1] == "not" or words[j-1] == "back"):
                    prime = False
                if word == words[j] and word.isdigit():
                    result.append(word)
                else:
                    result.append(word)
            if prime:
                result.append(word)
    return " ".join(result)
