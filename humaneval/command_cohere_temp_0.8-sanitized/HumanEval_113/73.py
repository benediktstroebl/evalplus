def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
          .replace('1', 'the number of odd elements in the string ')
          .replace('0', 'of the ')
          .replace('1', '1n')
          .replace('3', '3r')
          .replace('5', '5h')
          .replace('7', '7k')
          .replace('9', '9g')
          for s in lst]
    return r