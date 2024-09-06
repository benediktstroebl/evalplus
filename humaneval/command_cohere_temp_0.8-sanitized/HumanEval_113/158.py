def odd_count(lst):
    r = [str(len(re.findall(r'(\d)(?=(?:\d)(?!\1))', s)))
         .replace('n', '\n')
         .replace('n', 'n')
         .replace('1', 'the number of odd elements in the string 1 of the input.')
         .replace('4', 'the number of odd elements in the string 4 of the input.')
         .replace('8', 'the number of odd elements in the string 8 of the input.')
         for s in lst]
    return r