
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
    answer = ""
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if (words[i] != " " and words[j] != " " and is_prime(max(words[i], words[j]))) and (words[i] != words[j] or len(words[i]) != len(words[j])):
                answer += words[i] + " "
                break
    return answer