def find_max(words):
    max_dict = max(zip(words, map(set, words)), key=lambda x: (len(x[1]), x[0]))[0]
    return max_dict if len(max_dict) == len(set(max_dict)) else None