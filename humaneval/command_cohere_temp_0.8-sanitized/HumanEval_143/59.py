def words_in_sentence(sentence):
    sentence = sentence.strip().split()
    words = []
    for word in sentence:
      if len(word) == 1:
        words.append(word)
      else:
        isPrime = True
        for i in range(2, int(len(word)**0.5)+1):
          if word%i == 0:
            isPrime = False
            break
        if isPrime:
          words.append(word)
    return ' '.join(words)