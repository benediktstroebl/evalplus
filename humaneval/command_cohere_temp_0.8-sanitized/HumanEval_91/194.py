def is_bored(S):
    count = 0
    words = S.split()
    for i in range(len(words)):
        if words[i] == 'I':
            if i + 2 < len(words) and (words[i + 1] == '.' or words[i + 1] == '?' or words[i + 1] == '!'):
                count += 1
    return count