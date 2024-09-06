def check_dict_case(dict):
    if not dict:
        return False
    # Convert all keys to lowercase to check if all keys are in lowercase or all are in uppercase
    lowercase_dict = {key.lower(): value for key, value in dict.items()}
    return len(set(lowercase_dict.keys())) <= 1