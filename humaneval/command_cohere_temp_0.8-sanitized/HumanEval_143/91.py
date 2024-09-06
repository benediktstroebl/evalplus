def words_in_sentence(sentence):
    sentence = sentence.strip().split(' ')   
    words = []

    for word in sentence:
        if len(word) == 1:
            words.append(word)
        else:
            is_prime = True
            for num in range(2, int(len(word)**0.5)+1):
                if word%num == 0:
                    is_prime = False
                    break
            if is_prime:
                words.append(word)
                
    return ' '.join(words)