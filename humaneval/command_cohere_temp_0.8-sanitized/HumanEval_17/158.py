from typing import List
pattern = '^ {0,2}(?:o|o|)|(?:.|\.){1,3}'
formatter = r'(\d)({0,2}|{1,3})'
def parse_music(music_string: str) -> List[int]:
    result_list = []
    notes = re.findall(pattern, music_string)
    durations = re.findall(formatter, music_string)

    for i in range(len(notes)):
        result_list.append(int(durations[i]))

    return result_list