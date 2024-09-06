
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
    # Write your code here

    # 대소문자 구분 없이 처리
    sentence = sentence.lower()

    # 공백 문자열 제거
    sentence = sentence.strip()

    # 공백 문자열 리스트로 변환
    sentence_list = sentence.split()

    # 각 단어의 길이를 계산하여 배열에 저장
    word_length = []
    for word in sentence_list:
        word_length.append(len(word))

    # 배열의 원소가 소수인 경우 저장
    prime_word = []
    for i in range(len(word_length)):
        if word_length[i] % 2 != 0 and is_prime(word_length[i]):
            prime_word.append(sentence_list[i])

    # 결과 문자열 생성
    result_string = " ".join(prime_word)

    return result_string
