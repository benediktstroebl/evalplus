from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''.join(strings)
    return result
test_list = []
result = concatenate(test_list)