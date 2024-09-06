import re
def parse_music(music_string: str) -> List[int]:
    beat_pattern = re.compile(r'o+(?=\||.*)|o|.|o+')
    return [len(x.group()) for x in beat_pattern.finditer(music_string)]