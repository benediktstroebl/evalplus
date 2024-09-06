def anti_shuffle(s):
    words = s.split()
    word_asciival = [chr(c) for c in sorted(s, key=lambda x: x.charCodeAt)]
    return ' '.join(words for _ in range(len(word_asciival)) if word_asciival[_] == words[_])