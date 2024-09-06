from typing import List
PATTERN = "/(?P<whole>o)(?P<half>o|)|(?P<quarter>.)/"
def parse_music(music_string: str) -> List[int]:
    return [len(re.findall(PATTERN, e)) for e in music_string.split(' ')]