from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    paren_list = paren_string.split(')')
    paren_list = [sub for sub in paren_list if sub != '']
    return paren_list