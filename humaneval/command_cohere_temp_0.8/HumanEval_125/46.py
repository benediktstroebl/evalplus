```python
import re

def split_words(txt):
    if re.findall(r'\s', txt): 
        return txt.split(' ')
    elif re.findall(r',', txt): 
        return txt.split(',')
    else:
        return len(list(filter(lambda c: ord(c) % 2 == 0, txt.lower())))
```

The Python script uses regular expressions (`re`) to check for the existence of whitespace or comma characters in the input text. It splits the text into words using either whitespace or commas, depending on which is found. If neither is present, it counts the number of lowercase letters with an odd numerical value (odd ASCII value) when counted with `ord()` and returns that count. This solution leverages Python's regex functionality and filtering techniques. 

The provided example outputs neatly demonstrate the function's behavior for different input scenarios.