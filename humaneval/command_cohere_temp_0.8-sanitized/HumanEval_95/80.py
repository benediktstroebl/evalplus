def check_dict_case(dictn):
    test_cases = [
        {"a":"apple", "b":"banana"}, 
        {"a":"apple", "A":"banana", "B":"banana"}, 
        {"a":"apple", 8:"banana", "a":"apple"}, 
        {"Name":"John", "Age":"36", "City":"Houston"},
        {"STATE":"NC", "ZIP":"12345"}
    ]
    
    if not dictn or not isinstance(dictn, dict):
        return False
    elif len(dictn) == 0:
        return False
    else:
        true_lists = [['a','b'], ['A','B'], ['a','A'], ['Name','Age','City']]
        false_lists = [['a','A'], ['Name','Age','City'], ['STATE','ZIP']]
        # iterating over keys in the dictionary
        for key in dictn:
            # checking whether the key is lower or upper case
            if dictn[key].lower() != key.lower():
                # finding the index of the current key in the true/false list
                for i in range(0,len(true_lists)):
                    temp_list = true_lists[i].copy()
                    temp_list.remove(key)
                    if key in temp_list:
                        true_lists[i].append(key)
                        break
                    else:
                        temp_list = false_lists[i].copy()
                        temp_list.remove(key)
                        if key in temp_list:
                            false_lists[i].append(key)
                            break
                # if the key doesn't exist in any list, the function returns false
                if key not in true_lists[0] and key not in true_lists[1]:
                    return False
            else:
                true_lists.append([key])
        # checking if all lists have the same case (either lower or upper)
        for i in range(0,len(true_lists)):
            if len(true_lists[i]) == len(true_lists[0]):
                # if yes, the function returns True
                return True
            elif len(true_lists[i]) > 0:
                # if one list has no element, the function returns False
                return False
        return False