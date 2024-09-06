def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
         .replace('1', 'the number of odd elements in the string 1 of the input.')
         .replace('3', 'the number of odd elements in the string 3 of the input.')
         .replace('5', 'the number of odd elements in the string 5 of the input.')
         .replace('7', 'the number of odd elements in the string 7 of the input.')
         .replace('9', 'the number of odd elements in the string 9 of the input.')
         for s in lst]
    return r