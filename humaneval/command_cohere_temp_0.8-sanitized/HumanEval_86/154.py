def anti_shuffle(s):
    # Split the string into individual words and sort them
    words = sorted(s.split())
    
    # Join the sorted words back to form a new string
    return ' '.join(words)