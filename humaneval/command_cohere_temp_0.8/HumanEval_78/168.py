```python
import re

def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37']
    return sum(1 for x in re.findall('..?'+ '|'.join(primes), num))
```

The function uses a regular expression to match all the prime numbers from the list of hexadecimal digits. Under the hood, the `re.findall()` function goes through each digit in the provided number `num`, and for each digit, it checks whether it is a prime number. The `re.findall()` function returns a list of all prime digits matched, and the `sum()` function returns their count. 

Let's break down the regular expression: 
- `.` — Matches any single character (digit or symbol). 
- `??` — Matches an optional pair of characters, this is done to match single digit prime numbers, for example, '3'. 
- `|` — Indicates an OR expression, matching the subsequent primality checks against symbols. 
- `'...'` — This is a character class, it matches any three characters (digits or symbols). 
- `|` — Indicates an OR expression, matching the subsequent primality checks against digits. 

The regular expression works as follows:
- Matches one or more digits (optional pair allowed): "2", "11", "A3", "1F7". 
- Matches one or more prime symbols: "11", "B5", "D13", "7EF". 
- Matches either of the above options, example: "2B5", "11D". 

The total count of prime digits or symbols is then returned by the function. 

This problem can also be solved by first converting the hexadecimal number to a decimal number, then checking its primality, and finally converting the prime numbers back to hexadecimal. However, this solution is less efficient and thus less optimal. 

The code can be improved further by using a hash set instead of a list of prime numbers, and optimizing the regular expression, but it still will not qualify as a 'linear' solution.