def vowels_count(s):
    return sum(1 for c in s if c.lower() in 'aeiou')