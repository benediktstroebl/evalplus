```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    
    pattern = r'\(\d+\)\s(\oo|.\|)'
    matches = re.py.match(pattern, multiples, note in notes)
    
    return [int(multiples[0]), int(multiples[1])] for multiples in matches.

# Unit tests
test_parse_music = []
test_parse_music.push('o string of 4 o's')
test_parse_music.push('string of 4 o|'s')
test_parse_music.push('string of 2 o|s, 2 o s, 1 o')
test_parse_music.push('string of 2 o o s, 2 o o s')
test_parse_music.push('string of 4 o o o s')

test_parse_music = [test_parse_music[0]] + '\n'.join(test_parse_music)

for test in test_parse_music:
    actual = parse_music(test)
    print(f'Input: {test}\nOutput: {actual}')
```