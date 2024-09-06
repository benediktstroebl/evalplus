def check_dict_case(dict):
    if not dict:
        return False
    # Convert dictionary keys to lowercase and remove any duplicate keys
    lowercase_dict = {key: val for key, val in dict.items()}
    lowercase_dict = {k: v for k, v in lowercase_dict.items()}
    # Convert dictionary keys to uppercase and remove any duplicate keys
    uppercase_dict = {key: val for key, val in dict.items()}
    uppercase_dict = {k: v for k, v in uppercase_dict.items()}
    # Check if the lowercase and uppercase dictionaries contain the same keys
    return len(lowercase_dict) == len(uppercase_dict)