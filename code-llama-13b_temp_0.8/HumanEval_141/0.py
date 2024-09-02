
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """

    # code here
    # 1. 문장에서 알파벳이 아닌 것들을 필터링
    # 2. 알파벳으로 필터링된 문장을 슬라이싱 후, 알파벳 문자가 첫번째가 아니면 리턴
    # 3. 알파벳 문자가 첫번째이지만, 뒤에 점이 없으면 리턴
    # 4. 점을 발견했을 때, 앞뒤 길이가 맞는지 확인
    # 5. 앞뒤 길이가 맞고, 뒤에 확장자가 맞는지 확인
    alphapets = "".join(list(filter(lambda x: x.isalpha(), file_name)))
    if len(alphapets) == 0 or not file_name[0].isalpha():
        return 'No'

    if not "." in file_name:
        return 'No'

    first, second = file_name.split('.')
    if len(first) == 0:
        return 'No'

    if second not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'
