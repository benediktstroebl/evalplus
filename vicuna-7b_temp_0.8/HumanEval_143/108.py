
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
    word_list = sentence.split()
    new_list = []
    for word in word_list:
        if len(word) > 1:
            if (word[0] == word[-1] == ' '):
                continue
            prime_length = [i for i in range(1,len(word)+1) if word[i:i+2] != ' ']
            new_list.append(prime_length)
    return " ".join([word for word in word_list for prime_length in new_list if word in [str(i) for i in range(1, len(word) + 1)]])

sentence = input()
