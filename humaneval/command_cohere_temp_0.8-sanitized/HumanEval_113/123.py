def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
          for s in lst]
    return ['the number of odd elements ' + r[i] + ' the string ' + r[i] + ' of the input.'
            for i in range(len(r))]