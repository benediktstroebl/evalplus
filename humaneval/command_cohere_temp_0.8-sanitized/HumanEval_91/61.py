def is_bored(S):
    count = 0
    sentences = S.split('。')  
    for sentence in sentences:  
        sentence = sentence.strip()
        if len(sentence) > 0 and sentence[0] == 'I':
            if (sentence[1] == ' ' or sentence[1] == '.' or sentence[1] == '?' or sentence[1] == '!' or sentence[1] == '？'):
                count += 1  
    return count