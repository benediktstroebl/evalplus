def check_dict_case(dict):
    if not dict:
        return False
    # convert keys to lower case and remove any duplicate keys
    lower_dict = {k.lower(): v for k, v in dict.items()}
    # convert keys to upper case and remove any duplicate keys
    upper_dict = {k.upper(): v for k, v in dict.items()}
    return (lower_dict == upper_dict) or (len(set(lower_dict.keys()) & set(upper_dict.keys())) == len(lower_dict or upper_dict))