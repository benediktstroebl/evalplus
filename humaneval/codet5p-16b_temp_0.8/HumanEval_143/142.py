
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

    words = sentence.split(' ')
    words_prime = []
    for word in words:
        if len(word) == 1:
            continue
        for letter in word:
            if ord(letter) not in range(97, 123):
                break
        else:
            if not ''.join(sorted(word)) == word:
                continue
            if len(word) in (4, 5) or int(word[0]) in (4, 6) and int(word[1]) not in (4, 6) and int(word[2]) not in (4, 6) and int(word[3]) not in (4, 6):
                words_prime.append(word)

    return''.join(words_prime)
