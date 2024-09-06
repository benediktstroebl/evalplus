
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
    prime = [True] * (101)
    prime[0] = prime[1] = False
    for i in range(2, 100):
        if prime[i]:
            j = i * 2
            while j < 101:
                prime[j] = False
                j += i
    sentence_arr = sentence.split(" ")
    result = ""
    for word in sentence_arr:
        if prime[len(word)]:
            result += word + " "
    if result:
        result = result.rstrip()
    return result

