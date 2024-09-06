```python
import re

PRIMES = set('23579BDF')

def hex_key(num):
    return sum(1 for x in re.findall('..'?,'{0:X}'.format(int(num, 16))) if x in PRIMES)
```

The function `hex_key()` uses the regular expression `re.findall('..'?,'{0:X}'.format(int(num, 16)))` to match hexadecimal digits in the input num. The format specification `{0:X}` converts the integer representation of `num` to its hexadecimal format. The `int(num, 16)` converts the hexadecimal string `num` to its integer representation, and the `format()` method converts it to a string with hexadecimal digits. The `sum()` function then counts the number of matches, i.e., the number of prime hexadecimal digits, in `num`.

The PRIMES set stores the prime hexadecimal digits: 2, 3, 5, 7, B (decimal 11), D (decimal 13). The regular expression `..`? matches one or two digits, allowing for optional leading zeros. For example, the number `10` would be matched by `01`, and the number `100` would be matched by `001`. The `re.findall()` function returns a list of all matched digits, which the function then iterates through to check if each digit is prime. The `sum()` function then adds up the number of prime digits. 

This solution assumes the input is always correct or empty strings, and symbols `A,B,C,D,E,F` are always uppercase.

Note: The solution uses the set module, which is not included in the Python standard library in some environments, such as CodeOcean. If this is the case, you can replace the `set` with a list of prime digits, or alternatively, you can import the `set` module at the beginning of your code.