
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """

    new_text = text.replace(' ', '_')
    # 여기서는 ' ' 하나를 _로 대체하는 것 뿐이다. 여기서 나머지 2개의 공백을 포함한 모든 공백을 -로 바꿀 수 있다.
    # 빈 문자열이 포함되어 있는지 확인하고 없는 경우를 처리하지 않는다.
    if ' ' in new_text:
        new_text = new_text.replace('  ', '-')
    return new_text

    # 내 답
    def fix_spaces(text):
        # 공백 문자열을 리스트로 변환
        text_list = list(text)
        # 공백 문자열의 위치를 저장하는 리스트
        space_indices = []

        # 공백 문자열의 위치를 �
