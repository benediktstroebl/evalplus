def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
         for s in lst]
    return ['the number of odd elements ' + ''.join(map(str, i)) + ' in the string ' + ''.join(map(str, j)) + ' of the input'
            for i, j in zip(r, lst)]