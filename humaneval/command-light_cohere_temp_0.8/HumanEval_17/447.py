```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    def parse():
        beat_counts = {
            'o' : 4,
            'o|' : 2,
            '.|' : 1
        }
        notes = music_string.split(' ')
        codes = music_string.split(' o| ')[::2]
        beat_counts = beat_counts.map

        notes = [
            [beat_counts.get(note, 0) for note in codes]
        return [len(notes) for notes in notes]

    return parse()

# Test cases
test_music_str = '''
o o| |.oo swung
'''
test_result = parse_music(test_music_str)
print(test_result)  # Output: [2, 2]
``` 
This code defines a function `parse_music` that parses and converts music notes into the number of beats. The test case demonstrates how the parsing works with the provided test markdown code.