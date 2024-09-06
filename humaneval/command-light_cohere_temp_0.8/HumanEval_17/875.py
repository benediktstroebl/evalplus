```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.|' : 1}
    time_signature = next((ts for ts in music_string.split(' '|') if ts),
    beats = [notes[int(ts.strip()) for ts in time_signature.split('o approached with monatomic notes)

    beats.append(notes) if time_signature == '|')
    return [beat * beats[i] for i,beat in enumerate('beat')]

# Test cases
parse_music('o o| .| o| .| .| .| .| o o')
# [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
parse_music('.')
# []
parse_music('o o o| |')
# [4, 2, 2, 2]
parse_music('.).o')
# []
parse_music(' .")
# []
parse_music('o/o|o o|')
# [1, 4, 2, 1]
```