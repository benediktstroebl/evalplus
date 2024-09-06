```python
def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
          .replace('1', 'the number of odd elements in the string ')
          .replace('0', 'of the ')
          .replace('3', 'the number of odd elements ')
          .replace('2', 'the number of even elements ')
          .replace(str(i), 'the i\'th string of the input.')
          for i, s in enumerate(lst)]
    return r
```

The above solution utilizes regular expressions to match each digit and counts the odd ones. The final output is formatted using string replacements to provide the desired result. Note that this solution assumes that the input list contains strings consisting only of digits. If the input may contain other characters, additional processing would be necessary.