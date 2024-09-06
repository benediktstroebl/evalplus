from typing import List
def concatenate(strings: List[str]) -> str:
    concatenated_string = ''
    for string in strings:
        concatenated_string += f"{string}"
    return concatenated_string