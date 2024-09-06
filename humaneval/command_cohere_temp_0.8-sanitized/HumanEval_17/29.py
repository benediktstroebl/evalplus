from typing import List
PATTERN = "/(?P<whole>o)(?P<half>o|)|(?P<quarter>.)/"
def parse_music(music_string: str) -> List[int]:
    return [
        len(re.findall(PATTERN.format(whole='*' if i % 2 == 0 else '',
                                      half='*' if i % 3 == 0 else '',
                                      quarter='*' if i % 4 == 0 else ''),
                        music_string))
        for i in range(len(music_string))
    ]