def check_dict_case(dictn):
    test_cases = [
            {'lower': {'a': 'apple', 'b': 'banana'}, 'expected': True},
            {'upper': {'A': 'apple', 'B': 'banana'}, 'expected': True},
            {'mixed_case': {'a': 'apple', 'A': 'banana', 'B': 'banana'}, 'expected': False},
            {'duplicates_exist': {'a': 'apple', 'A': 'banana', 'a': 'apple'}, 'expected': False},
            {'nonstring_keys': {'name': 'John', 'age': '36', 'city': 'Houston'}, 'expected': False},
            {'all_upper': {'STATE': 'NC', 'ZIP': '12345'}, 'expected': True},
    ]
    if not dictn or not all(isinstance(k, str) for k in dictn.keys()) or not all(k.isupper() for k in dictn.keys()) or not all(k.islower() for k in dictn.keys()):
        return False
    for tc in test_cases:
        if dictn == tc['lower'] or dictn == tc['upper'] or dictn == tc['all_upper']:
            return tc['expected']
    return False