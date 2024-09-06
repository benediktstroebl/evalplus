from typing import List
def parse_music(music_string: str) -> List[int]:
    MOD = 4  # the base duration (whole note) lasts this many beats
    LEG = 'o|' if __web__ else 'o' # the legend char, 'o|' for web, 'o' for console
    beat_list = []
    cur_beat = None
    cur_note = 0
    
    for char in music_string:
        if char == LEG:
            if cur_beat is not None:
                beat_list.append(cur_note)
            cur_beat = None
            cur_note = 0
        elif char == '.|':
            cur_note += 1
        elif char == ' ':
            if cur_beat is not None:
                beat_list.append(cur_note)
            cur_beat = None
            cur_note = 0
        elif char == '-':
            if cur_beat is not None:
                beat_list.append(cur_note)
            cur_beat = None
            cur_note = 2
        elif char == '|':
            cur_beat += 1
        else:
            print(f'ERROR: {char}')
            return None

    if cur_beat is not None:
        beat_list.append(cur_note)

    return beat_list